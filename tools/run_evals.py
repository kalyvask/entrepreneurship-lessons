#!/usr/bin/env python3
"""LLM-judge eval runner for the ent-* skills.

For each fixture in evals/cases/:
  1. Load the skill's SKILL.md as the system prompt (prompt-cached).
  2. Send the fixture `input` to a candidate model.
  3. Have a judge model decide, per assertion, whether the behaviour is present.
  4. Majority-vote across N judges.

The GATE is deliberately narrow: the build fails only on a `must_not` hit — an
anti-pattern the response actually exhibited. `expect` misses are reported as
warnings, not failures, because a free-text coaching response can satisfy the
spirit of an `expect` in wording a judge scores conservatively. Anti-patterns
are the clean signal (see evals/README.md).

This is NOT the PR gate. It needs ANTHROPIC_API_KEY and costs tokens; run it on
demand (`python tools/run_evals.py`) or on a schedule. With no API key it exits
0 with a skip notice, so it never blocks a fork PR.

Usage:
  python tools/run_evals.py [--candidate MODEL] [--judge MODEL] [--votes N]
                            [--case ID ...] [--json report.json]

Deps: pip install anthropic pyyaml
"""
import argparse
import glob
import json
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("pyyaml required: pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES = os.path.join(ROOT, "evals", "cases")

CANDIDATE_MODEL = "claude-opus-4-8"
JUDGE_MODEL = "claude-sonnet-4-6"

JUDGE_SYSTEM = (
    "You are a strict evaluator of an entrepreneurship-coaching AI's response. "
    "You are given the founder's input, the assistant's response, and a list of "
    "behavioural assertions. For each assertion decide ONLY whether that behaviour "
    "is genuinely PRESENT in the response. Judge substance, not wording — but do "
    "not give credit for a behaviour the response does not actually show. Default "
    "to present=false when uncertain. Return your verdicts in the required schema."
)

VERDICT_SCHEMA = {
    "type": "object",
    "properties": {
        "verdicts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "present": {"type": "boolean"},
                    "reason": {"type": "string"},
                },
                "required": ["id", "present", "reason"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["verdicts"],
    "additionalProperties": False,
}


def load_cases(only):
    cases = []
    for path in sorted(glob.glob(os.path.join(CASES, "*.yaml"))):
        data = yaml.safe_load(open(path, encoding="utf-8"))
        if only and data.get("id") not in only:
            continue
        cases.append(data)
    return cases


def skill_system(skill_name):
    p = os.path.join(ROOT, ".claude", "skills", skill_name, "SKILL.md")
    if not os.path.exists(p):
        raise FileNotFoundError(f"skill not found: {skill_name} ({p})")
    return open(p, encoding="utf-8").read()


def run_candidate(client, skill_md, user_input):
    resp = client.messages.create(
        model=CANDIDATE_MODEL,
        max_tokens=4000,
        thinking={"type": "adaptive"},
        output_config={"effort": "medium"},
        system=[{"type": "text", "text": skill_md, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_input}],
    )
    return "".join(b.text for b in resp.content if b.type == "text")


def run_judge(client, founder_input, response_text, assertions):
    # assertions: list of {id, kind, text}
    numbered = "\n".join(f'{a["id"]}. [{a["kind"]}] {a["text"]}' for a in assertions)
    user = (
        f"FOUNDER INPUT:\n{founder_input}\n\n"
        f"ASSISTANT RESPONSE:\n{response_text}\n\n"
        f"ASSERTIONS (decide present=true/false for each by id):\n{numbered}"
    )
    resp = client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=2000,
        thinking={"type": "disabled"},
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": VERDICT_SCHEMA}},
        system=[{"type": "text", "text": JUDGE_SYSTEM, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user}],
    )
    text = next(b.text for b in resp.content if b.type == "text")
    return {v["id"]: v for v in json.loads(text)["verdicts"]}


def evaluate(client, case, votes):
    skill_md = skill_system(case["skill"])
    response_text = run_candidate(client, skill_md, case["input"])

    assertions = []
    for i, t in enumerate(case.get("expect", [])):
        assertions.append({"id": i, "kind": "expect", "text": t})
    for j, t in enumerate(case.get("must_not", []), start=len(assertions)):
        assertions.append({"id": j, "kind": "must_not", "text": t})

    # Majority vote across `votes` judges.
    tallies = {a["id"]: 0 for a in assertions}
    for _ in range(votes):
        verdicts = run_judge(client, case["input"], response_text, assertions)
        for a in assertions:
            if verdicts.get(a["id"], {}).get("present"):
                tallies[a["id"]] += 1

    majority = (votes // 2) + 1
    expect_results, must_not_hits = [], []
    for a in assertions:
        present = tallies[a["id"]] >= majority
        if a["kind"] == "expect":
            expect_results.append((a["text"], present))
        else:
            if present:  # an anti-pattern that IS present == a failure
                must_not_hits.append(a["text"])

    return {
        "id": case["id"],
        "skill": case["skill"],
        "response_chars": len(response_text),
        "expect": [{"text": t, "satisfied": ok} for t, ok in expect_results],
        "expect_passed": sum(1 for _, ok in expect_results if ok),
        "expect_total": len(expect_results),
        "must_not_hits": must_not_hits,
        "passed": not must_not_hits,  # the gate
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", default=CANDIDATE_MODEL)
    ap.add_argument("--judge", default=JUDGE_MODEL)
    ap.add_argument("--votes", type=int, default=3)
    ap.add_argument("--case", action="append", default=[], help="fixture id (repeatable)")
    ap.add_argument("--json", help="write a JSON report to this path")
    args = ap.parse_args()

    global CANDIDATE_MODEL, JUDGE_MODEL
    CANDIDATE_MODEL, JUDGE_MODEL = args.candidate, args.judge

    if not (os.getenv("ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_AUTH_TOKEN")):
        print("ANTHROPIC_API_KEY not set — skipping LLM-judge evals (not a failure).")
        print("This runner is opt-in; the PR gate is the deterministic content checks.")
        return 0

    try:
        import anthropic
    except ImportError:
        sys.exit("anthropic required: pip install anthropic")
    client = anthropic.Anthropic()

    cases = load_cases(set(args.case))
    if not cases:
        sys.exit("no fixtures found")

    print(f"Running {len(cases)} fixtures | candidate={CANDIDATE_MODEL} judge={JUDGE_MODEL} votes={args.votes}\n")
    results, gate_failures = [], 0
    for case in cases:
        try:
            r = evaluate(client, case, args.votes)
        except Exception as e:  # one bad fixture shouldn't abort the suite
            print(f"  ERROR  {case.get('id', '?')}: {e}")
            results.append({"id": case.get("id"), "error": str(e), "passed": False})
            gate_failures += 1
            continue
        mark = "PASS" if r["passed"] else "FAIL"
        if not r["passed"]:
            gate_failures += 1
        print(f"  {mark}  {r['id']}  (expect {r['expect_passed']}/{r['expect_total']})")
        for t, ok in [(e["text"], e["satisfied"]) for e in r["expect"]]:
            if not ok:
                print(f"         . expect missed (warning): {t}")
        for t in r["must_not_hits"]:
            print(f"         x MUST-NOT hit (gate): {t}")
        results.append(r)

    if args.json:
        json.dump({"results": results}, open(args.json, "w", encoding="utf-8"), indent=2)
        print(f"\nReport written to {args.json}")

    print(f"\n{len(cases) - gate_failures}/{len(cases)} passed the gate (no must_not hits).")
    if gate_failures:
        print("GATE FAILED: a response exhibited a forbidden anti-pattern.")
        return 1
    print("Gate OK. (Expect-misses above are advisory, not failures.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
