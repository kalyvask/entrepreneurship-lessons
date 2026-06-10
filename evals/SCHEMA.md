# Fixture schema

Every file in `cases/` is a single YAML document describing one behavioural fixture. This doc
defines the required structure so CI and contributors can validate fixture **well-formedness**
(not correctness of any skill — see `README.md`).

## Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `id` | string | Non-empty. Unique across `cases/`. Should match the filename stem (e.g. file `foo.yaml` → `id: foo`). Lowercase kebab-case. |
| `skill` | string | Non-empty. Must name one of the repo's skills: `ent-stage-router`, `ent-pmf-evaluator`, `ent-unit-econ-check`, `ent-office-hours`, `ent-concept-test`, `ent-mvp-scoper`, `ent-red-team`, `ent-intake`, `ent-pivot-coach`, `ent-thesis`, `ent-career-coach`. |
| `intent` | string | Non-empty. One line: what this fixture is checking. |
| `input` | string | Non-empty. The founder's words and/or data, verbatim, as it would be pasted to the skill. |
| `expect` | list of strings | At least 1 item. Each item is one behaviour the response MUST show. |
| `must_not` | list of strings | At least 1 item. Each item is one anti-pattern the response MUST avoid. |
| `rationale` | string | Non-empty. Why these expectations hold, citing the relevant skill's `SKILL.md`, `../rubrics/journey_rubrics.md`, and/or the PMF vocabulary in `../README.md`. |

No other top-level fields are required. Extra fields are allowed but should be intentional.

## Shape rules (what a validator should check)

- File parses as YAML and is a single mapping (not a list, not a stream of documents).
- All seven required keys are present.
- `id`, `skill`, `intent`, `input`, `rationale` are non-empty strings.
- `skill` is one of the allowed values listed above.
- `expect` and `must_not` are each a non-empty list, and every element is a non-empty string.
- `id` is unique across all files in `cases/`.

Well-formedness is necessary but **not** sufficient: a valid fixture still has to be graded by a
human or LLM judge against a real skill response. CI validating these rules does not mean any
skill passes.

## Minimal example

```yaml
id: example-case
skill: ent-pmf-evaluator
intent: One line describing what behaviour this fixture checks.
input: |
  The founder's words and data, pasted verbatim.
expect:
  - A behaviour the response must show.
  - Another required behaviour.
must_not:
  - An anti-pattern the response must avoid.
rationale: >
  Why the expectations hold, citing the skill's own SKILL.md, the stage rubric, or the PMF
  vocabulary in the root README.
```

## Reference validator (optional)

A contributor can validate locally with any YAML loader. Sketch in Python:

```python
import sys, glob, yaml

ALLOWED_SKILLS = {
    "ent-stage-router", "ent-pmf-evaluator", "ent-unit-econ-check",
    "ent-office-hours", "ent-concept-test", "ent-mvp-scoper", "ent-red-team",
    "ent-intake", "ent-pivot-coach", "ent-thesis", "ent-career-coach",
}
REQUIRED_STR = ("id", "skill", "intent", "input", "rationale")

def nonempty_str(x): return isinstance(x, str) and x.strip() != ""

def str_list(x):
    return isinstance(x, list) and len(x) > 0 and all(nonempty_str(i) for i in x)

seen, ok = set(), True
for path in glob.glob("cases/*.yaml"):
    doc = yaml.safe_load(open(path, encoding="utf-8"))
    errs = []
    if not isinstance(doc, dict):
        errs.append("not a single YAML mapping")
        doc = {}
    for k in REQUIRED_STR:
        if not nonempty_str(doc.get(k)):
            errs.append(f"missing/empty string field: {k}")
    if doc.get("skill") not in ALLOWED_SKILLS:
        errs.append(f"skill not in allowed set: {doc.get('skill')!r}")
    for k in ("expect", "must_not"):
        if not str_list(doc.get(k)):
            errs.append(f"{k} must be a non-empty list of non-empty strings")
    cid = doc.get("id")
    if nonempty_str(cid):
        if cid in seen:
            errs.append(f"duplicate id: {cid}")
        seen.add(cid)
    if errs:
        ok = False
        print(f"FAIL {path}")
        for e in errs:
            print(f"  - {e}")

sys.exit(0 if ok else 1)
```
