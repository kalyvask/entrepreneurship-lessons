#!/usr/bin/env python3
"""Validate venture workspaces against the contract in scaffold/README.md.

Strict mode (the filled example, examples/example-venture):
  - all workspace files exist
  - founder-state.yaml parses, has the required keys, a valid stage id, and
    integer gate scores in 0..3
  - the evidence gate: every gate score of 2-3 carries an inline citation
    comment on its line ("a 2-3 needs a cited artifact, not a claim")
  - history rows are well-formed (date/to/why) and dates never go backwards
    (the append-only smell test)

Lenient mode (the blank scaffold template): files exist, YAML parses, the
stage id is valid. Blank values are fine — a template is allowed to be empty,
but its shape may not drift from the contract.

Usage:
  python tools/check_state.py                  # strict example-venture + lenient scaffold
  python tools/check_state.py PATH [PATH ...]  # strict on the given workspace dirs
"""
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("pyyaml required: pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_FILES = [
    "founder-state.yaml",
    "lof_ledger.md",
    "interviews.csv",
    "experiment_log.md",
    "rubric_scores.md",
    "pmf_dashboard.md",
    "decision_dossier.md",
    "hypotheses.md",
    "thesis_ledger.md",
]
REQUIRED_KEYS = [
    "venture", "one_liner", "updated", "stage",
    "leap_of_faith", "narrow_who", "blockers", "history",
]


def stage_ids():
    data = yaml.safe_load(open(os.path.join(ROOT, "library.yaml"), encoding="utf-8"))
    return {a["id"] for a in data["artifacts"] if a.get("kind") == "stage"}


def gate_score_lines(raw):
    """Yield (lineno, key, score, has_comment) for lines inside the gate_scores block."""
    in_block, indent = False, 0
    for i, ln in enumerate(raw.splitlines(), 1):
        m = re.match(r"^(\s*)gate_scores:\s*(.*)$", ln)
        if m:
            rest = m.group(2).split("#", 1)[0].strip()
            # `gate_scores: {}` (inline empty map) has no block to scan
            in_block = rest == ""
            indent = len(m.group(1))
            continue
        if in_block:
            if ln.strip() == "" or ln.strip().startswith("#"):
                continue
            cur = len(ln) - len(ln.lstrip())
            if cur <= indent:
                in_block = False
                continue
            sm = re.match(r"^\s*([A-Za-z0-9_]+):\s*(\d+)\s*(#.*)?$", ln)
            if sm:
                yield i, sm.group(1), int(sm.group(2)), bool(sm.group(3))


def check_workspace(path, strict, stages):
    errs = []
    if not os.path.isdir(path):
        return [f"workspace dir missing: {path}"]

    for f in REQUIRED_FILES:
        if not os.path.exists(os.path.join(path, f)):
            errs.append(f"missing file: {f}")

    fs = os.path.join(path, "founder-state.yaml")
    if not os.path.exists(fs):
        return errs
    raw = open(fs, encoding="utf-8").read()
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        errs.append(f"founder-state.yaml does not parse: {e}")
        return errs
    if not isinstance(data, dict):
        errs.append("founder-state.yaml is not a YAML mapping")
        return errs

    for k in REQUIRED_KEYS:
        if k not in data:
            errs.append(f"founder-state.yaml missing key: {k}")

    stage = data.get("stage") or {}
    cur = stage.get("current") if isinstance(stage, dict) else None
    if cur not in stages:
        errs.append(f"stage.current is not a valid stage id: {cur!r}")

    if not strict:
        return errs

    # gate scores: ints 0..3, and the evidence gate on 2-3
    gs = stage.get("gate_scores") if isinstance(stage, dict) else None
    if not isinstance(gs, dict) or not gs:
        errs.append("stage.gate_scores must be a non-empty mapping in a filled workspace")
    else:
        for k, v in gs.items():
            if not isinstance(v, int) or not (0 <= v <= 3):
                errs.append(f"gate score {k!r} must be an integer 0..3 (got {v!r})")
    for lineno, key, score, has_comment in gate_score_lines(raw):
        if score >= 2 and not has_comment:
            errs.append(
                f"evidence gate: '{key}: {score}' (founder-state.yaml line {lineno}) "
                "has no inline citation comment"
            )

    hist = data.get("history")
    if not isinstance(hist, list) or not hist:
        errs.append("history must be a non-empty list in a filled workspace")
    else:
        prev = ""
        for idx, row in enumerate(hist):
            if not isinstance(row, dict) or not all(
                str(row.get(k) or "").strip() for k in ("date", "to", "why")
            ):
                errs.append(f"history[{idx}] needs non-empty date / to / why")
                continue
            d = str(row["date"])
            if prev and d < prev:
                errs.append(f"history dates go backwards at row {idx} ({d} after {prev})")
            prev = d

    if not isinstance(data.get("blockers"), list):
        errs.append("blockers must be a list")

    return errs


def main():
    stages = stage_ids()
    targets = sys.argv[1:]
    if targets:
        jobs = [(t, True) for t in targets]
    else:
        jobs = [
            (os.path.join(ROOT, "examples", "example-venture"), True),
            (os.path.join(ROOT, "scaffold"), False),
        ]

    failed = False
    for path, strict in jobs:
        label = os.path.relpath(path, ROOT)
        errs = check_workspace(path, strict, stages)
        if errs:
            failed = True
            print(f"WORKSPACE CONTRACT FAILED: {label}")
            for e in errs:
                print(f"  - {e}")
    if failed:
        return 1
    print(
        "workspace contract OK: "
        + ", ".join(
            f"{os.path.relpath(p, ROOT)} ({'strict' if s else 'lenient'})" for p, s in jobs
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
