# The Venture Workspace

The rest of this repo is a knowledge base — frameworks, playbooks, rubrics, skills. This
folder is the **state**: the small set of files that hold *your* venture, so the agent
partner can pick up where you left off instead of re-diagnosing you every session.

Copy `scaffold/` into your own project. You don't fill these in by hand — **start by running
`/ent-intake`**, which interviews you, places you on the 00→07 map, and writes these files for you.
Every other skill reads this state first; if it doesn't exist yet, they send you to `/ent-intake`
before anything else (you can't read state that isn't there). A filled, end-to-end example lives in
[`examples/example-venture/`](../examples/example-venture/).

**Where this is heading.** PMF is the milestone, not the finish line. The destination is three
synthesized outputs you carry beyond this venture — your **PMF insights**, your **investment /
founder-style memo**, and your **value-hypothesis stance** — built by `/ent-thesis` into
`thesis_ledger.md`. The per-venture files below feed that cross-venture thesis.

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
| `thesis_ledger.md` | **Cross-venture, per person.** Durable learnings → your PMF insights, investment-style memo, and value-hypothesis stance | `ent-thesis` (keep one above all your ventures) |

## The one rule that makes this work

**A gate score of 2 or 3 requires a cited artifact in this workspace.** Not a feeling, not
"we talked to customers." A row in `interviews.csv`, a signed LOI, a line in
`experiment_log.md`, a number in `pmf_dashboard.md`. The rubric (`rubrics/journey_rubrics.md`)
is a mirror, not a trophy; this workspace is what keeps it honest. The agent will refuse to
advance a stage on an unevidenced score.

## How the agent uses it

You don't hand-fill these files. You talk to the agent; it writes them.

1. **Start with `/ent-intake`.** It interviews you — what you're working on, what evidence you
   have — places you on the 00→07 map, and writes `founder-state.yaml` for you. It scores the gates
   from the behaviour and numbers you describe, not from a self-rating, then reads the result back
   in plain English for you to confirm.
2. Each session after, `/ent-stage-router` reads your state and routes you to the next step; as you
   do the work, the relevant skill appends evidence to the files above. You never edit YAML by hand.
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
