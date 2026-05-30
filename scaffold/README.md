# The Venture Workspace

The rest of this repo is a knowledge base — frameworks, playbooks, rubrics, skills. This
folder is the **state**: the small set of files that hold *your* venture, so the agent
partner can pick up where you left off instead of re-diagnosing you every session.

Copy `scaffold/` into your own project (or run the installer) and fill it in as you go.
A filled, end-to-end example lives in [`examples/example-venture/`](../examples/example-venture/).

## The files

| File | What it holds | Maintained by |
|---|---|---|
| `founder-state.yaml` | Current stage, gate scores, leap of faith, blockers, transition history | `ent-stage-router` reads/writes; you confirm |
| `lof_ledger.md` | The one leap of faith, the test running against it, and its status over time | `ent-value-hypothesis-builder`, `ent-mvp-review` |
| `interviews.csv` | One row per customer conversation, scored on the four desperation markers (behaviour, not opinions) | `ent-customer-discovery`, `ent-interview-debrief` |
| `hypotheses.md` | Hypothesis tracker: evidence for, evidence against, what would change your mind | `ent-synthesis-coach` |
| `experiment_log.md` | Every concept / implementation / MVP test, with its **pre-registered** pass threshold and result | `ent-concept-test`, `ent-mvp-review` |
| `rubric_scores.md` | The stage gates, scored 0–3, each 2–3 backed by a **cited artifact** | `ent-stage-router`, `ent-pmf-evaluator` |
| `pmf_dashboard.md` | The only metrics that count at Stage 06 — and the vanity metrics we refuse to track | `ent-pmf-evaluator` |
| `decision_dossier.md` | A running, exportable record of the decisions you can defend (insight → problem → value hypothesis → pivots → PMF) | every gate; capstone is `ent-pmf-memo` |

## The one rule that makes this work

**A gate score of 2 or 3 requires a cited artifact in this workspace.** Not a feeling, not
"we talked to customers." A row in `interviews.csv`, a signed LOI, a line in
`experiment_log.md`, a number in `pmf_dashboard.md`. The rubric (`rubrics/journey_rubrics.md`)
is a mirror, not a trophy; this workspace is what keeps it honest. The agent will refuse to
advance a stage on an unevidenced score.

## How the agent uses it

1. Run `/ent-stage-router`. If `founder-state.yaml` is empty, it runs a short placement and
   seeds it (cold start). Otherwise it reads your state and routes you to the next step.
2. As you do the work, the relevant skill appends evidence to the workspace files above.
3. Before the highest-stakes gate (Stage 06 → 07, pivot-or-persevere), `/ent-red-team` fires
   automatically against your `lof_ledger.md` and `pmf_dashboard.md`.

## Engine metrics (optional, derivable from `founder-state.yaml` history)

Because state is logged, you can measure the *journey itself*, not just the venture:

- **Time-in-stage** — how long each gate took.
- **First-attempt gate-pass rate** — how often a stage passed without a return trip.
- **Cost-of-disconfirmation** — how cheaply a bad idea was killed (days/$ to a clean kill).
- **Evidence-to-decision latency** — time from "evidence in hand" to "decision logged".

These are for you, not a scoreboard. Low cost-of-disconfirmation is the goal: being wrong
cheap, fast, and on purpose.

## When guidance conflicts

This repo blends many sources. When they disagree (see `frameworks/conflicts.md`), the
**PMF learnings win**: desperation over need, behaviour over opinions, the narrow *who*,
the rate of learning over the rate of shipping. Score the evidence, not the hope.
