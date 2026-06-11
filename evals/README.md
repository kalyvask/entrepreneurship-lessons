# Evaluation suite — `ent-*` PMF skills

This directory holds an evaluation suite for the Claude Code skills in this repo
(`ent-stage-router`, `ent-pmf-evaluator`, `ent-unit-econ-check`, `ent-office-hours`,
`ent-concept-test`, `ent-mvp-scoper`, `ent-red-team`, `ent-intake`, `ent-pivot-coach`,
`ent-thesis`, `ent-career-coach`, `ent-diligence`).

## What these evals are

They are **behavioural fixtures**. Each fixture is a realistic founder situation (the
`input`) paired with the behaviour a correct skill response **must** show (`expect`) and the
anti-patterns it **must not** show (`must_not`). They test discipline, not exact wording: the
point is whether the skill refuses to let a founder fool themselves, in line with the PMF
principles documented in `../CLAUDE.md`.

## What these evals are NOT

- They are **not** an automated pass/fail check on model output in CI. There is no harness here
  that runs a skill and scores its answer. Grading the `expect` / `must_not` assertions against a
  real response requires judgement and is done by **a human reviewer or an LLM judge**.
- CI's only job (if you wire it up) is to validate that each fixture file is **well-formed** —
  that it has the required fields and they have the right shape. See `SCHEMA.md`. Well-formedness
  says nothing about whether any skill actually passes.

Do not read these files as "the skills are tested and green." They are graded inputs, not a test
result.

## A note on provenance

These fixtures were authored directly against the covered skills' own `SKILL.md` files under
`../.claude/skills/*/` and the stage rubrics in `../rubrics/journey_rubrics.md`. The
load-bearing specifics in each fixture were checked against the actual skill prose — e.g. the
concept-test "pre-pay / paid pilot / signed LOI" pass signals and its "not friends" rule, the
red-team "Marks 2x2 quadrant" and "name 3 people who'd push back" disconfirmation move, the
unit-econ formulas and the "loaded CAC, not founder-time-is-free" discipline, and the
pmf-evaluator's "what you DON'T accept" list (signups, one advocate, revenue-without-retention).

The overarching discipline these skills share is the repo's PMF through-line — **desperation not
need, behavior not opinions, narrow not broad, retention not signups**, plus the Sean Ellis 40%
line and >40% organic pull — stated in the root `../CLAUDE.md` and treated in full in
`../frameworks/pmf.md`. The `rationale` field of each fixture cites that vocabulary by name and
points at the specific skill behaviour it tests. If a `SKILL.md` is later revised, re-read it and
reconcile any fixture whose expectations have drifted from the prose.

## How to run one fixture (manual / LLM-judge loop)

1. Open a fixture in `cases/`, e.g. `cases/stage-router-no-over-advance.yaml`.
2. Read its `skill` field. Invoke that skill in Claude Code (e.g. `/ent-stage-router`).
3. Paste the fixture's `input` verbatim as the founder's message.
4. Capture the skill's full response.
5. Grade the response:
   - For **each** line in `expect`: did the response exhibit that behaviour? (yes / no / partial)
   - For **each** line in `must_not`: did the response avoid that anti-pattern? (avoided / violated)
6. A fixture **passes** only if every `expect` behaviour is present (at least "partial" with
   justification) **and** no `must_not` anti-pattern appears. A single `must_not` violation is a
   fail regardless of how many `expect` lines were met — the anti-patterns are the bright lines.

### Using an LLM as the judge

Give the judge model three things: the fixture's `input`, the skill's response, and the
fixture's `expect` + `must_not` lists. Ask it to return, per assertion, a verdict (`met` /
`partial` / `missing` for `expect`; `avoided` / `violated` for `must_not`) with a one-line
quote or paraphrase as evidence. Keep the judge blind to the `rationale` so it grades behaviour,
not intent. Treat the judge as advisory; a human should spot-check disagreements and any `partial`.

## Optional automated runner (LLM judge)

`tools/run_evals.py` automates the manual loop above with an LLM judge, for running the whole
suite at once. It is **opt-in and not the PR gate** — the deterministic content-integrity checks
remain the only thing every PR must pass.

```bash
pip install anthropic pyyaml
export ANTHROPIC_API_KEY=...        # without this, the runner exits 0 with a skip notice
python tools/run_evals.py           # all fixtures
python tools/run_evals.py --case unit-econ-broken-fails --votes 3
```

How it grades, and the honest limits:

- For each fixture it sends the `input` to a candidate model (default `claude-opus-4-8`) with the
  skill's `SKILL.md` as the system prompt, then asks a judge model (default `claude-sonnet-4-6`),
  per assertion, whether the behaviour is present. It majority-votes across `--votes` judges (default 3).
- **The gate is narrow: it fails only on a `must_not` hit** — an anti-pattern the response actually
  exhibited. `must_not` is the bright line. `expect` misses print as warnings, not failures, because
  a correct free-text response can satisfy an `expect` in wording a judge scores conservatively. So
  the runner enforces "never do the forbidden thing" and advises on "did the good thing".
- An LLM judge is **non-deterministic**; treat a single red as a prompt to look, not a verdict. That
  is why it is not wired into the PR gate.

CI: `.github/workflows/evals.yml` runs it on demand (Actions tab) and weekly, with
`ANTHROPIC_API_KEY` from repo secrets. Fork PRs don't get the secret, so the runner skips cleanly.

## Coverage

Thirteen fixtures, with positive and negative cases:

| # | id | skill | tests |
|---|----|-------|-------|
| 1 | `stage-router-no-over-advance` | `ent-stage-router` | refuses to confirm PMF on thin evidence; routes, does not advance |
| 2 | `pmf-evaluator-rejects-weak-evidence` | `ent-pmf-evaluator` | "not yet" verdict; rejects signups / one advocate / revenue-without-retention |
| 3 | `unit-econ-broken-fails` | `ent-unit-econ-check` | LTV/CAC ≈ 0.33 → broken; names retention; refuses free founder-time CAC |
| 4 | `unit-econ-healthy-passes` | `ent-unit-econ-check` | LTV/CAC = 6 → healthy; payback < 12mo; still flags pre-PMF caveat |
| 5 | `mvp-scoper-cuts-features` | `ent-mvp-scoper` | cuts 15 features to the leap-of-faith test; suggests concierge |
| 6 | `red-team-refutes-consensus` | `ent-red-team` | flags consensus; demands disconfirmers; cheaper explanation; biggest risk |
| 7 | `concept-test-rejects-vanity-threshold` | `ent-concept-test` | rejects waitlist threshold; requires pre-registered behavioural commitment |
| 8 | `office-hours-reframe` | `ent-office-hours` | Mom Test interrogation; reframes; narrow wedge; won't validate framing |
| 9 | `intake-no-over-place` | `ent-intake` | places on evidence, not self-assessment; refuses dictated scores; gaps become blockers |
| 10 | `pivot-coach-refuses-death-pivot` | `ent-pivot-coach` | catches the death-pivot; demands prior thresholds + over-performing slice before any new hypothesis |
| 11 | `thesis-rejects-anecdote` | `ent-thesis` | rule of three: n=1 stays a candidate; the log is append-only; no rewriting history |
| 12 | `career-coach-stays-off-spine` | `ent-career-coach` | coaches trajectory over title; routes venture validation back to the spine; never touches the workspace |
| 13 | `diligence-flags-unverified` | `ent-diligence` | refuses the rubber stamp; flags unsourced claims; decomposes vague numbers; routes the bear case to red-team |

Cases 3 and 4 are a matched negative/positive pair on the same skill, so a passing skill must
swing the verdict on the numbers alone.
