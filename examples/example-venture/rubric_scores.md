# Rubric Scores — the evidence-gated record

Score the current stage against `rubrics/journey_rubrics.md`: each dimension 0–3, advance
only when **every dimension ≥ 2 and none = 0**. The rule that makes this real:

> **Every score of 2 or 3 must cite a specific artifact in this workspace** — a row in
> `interviews.csv`, a line in `experiment_log.md`, a signed LOI, a number in
> `pmf_dashboard.md`. "We talked to customers" is a 1. "8 of 12 in our narrow segment had
> built a workaround and 3 pre-paid (interviews.csv rows 4–15)" is a 3.

Have someone allowed to disagree with you grade it too — a co-founder, an advisor, or
`/ent-red-team`. Founders systematically over-score their own who-narrowness and desperation
evidence.

> FILLED EXAMPLE (Croplane). One scored block per stage passed, newest at the top. The
> Stage 06 block honestly does NOT pass the PMF bar: Sean Ellis is below 40%.

---

## Current stage: Stage 06 — PMF Measurement

| Dimension | Score (0–3) | Cited evidence (artifact + ref) |
|---|---|---|
| Held narrow who | 3 | All 7 paying customers are inside the narrow who; metrics computed only against it (pmf_dashboard.md; founder-state narrow_who) |
| Sean Ellis | 2 | 38% "very disappointed", climbing from 26%, but below the 40% bar (pmf_dashboard.md) |
| Retention | 2 | 6 of 7 active at 12 weeks; curve flattening above zero, only 8 weeks flat, 1 revert (experiment_log EXP-04; pmf_dashboard.md) |
| Organic acquisition | 2 | ~35% of recent logos from peer referral, climbing from 0%, under the >40% bar (pmf_dashboard.md) |
| LOF verified | 2 | Willingness-to-pay verified by behaviour (5 of 8 paid in 30 days); retention depth not yet (experiment_log EXP-03/EXP-04; lof_ledger.md) |
| The tells | 2 | 2 of 3 present: unprompted referrals and a shrinking sales cycle; pricing power not yet tested |

**Gate:** all ≥ 2 and no 0s? **[x] yes  [ ] no** — gate to *stay credibly in Stage 06* is cleared, but **this is NOT PMF**: PMF needs Sean Ellis ≥ 40% with retention flattening. We are at 38%. Hold the who, deepen retention; do not advance to scaling.

---

## Stage 05 — MVP Build

| Dimension | Score (0–3) | Cited evidence (artifact + ref) |
|---|---|---|
| Usable & live | 3 | Real product used in the real Monday workflow; preceded by a live facade test (experiment_log EXP-02, EXP-03) |
| Smallest feature set | 3 | Scope cut to the daily cut list; weekly planner removed when unused (hypotheses H4; lof_ledger.md) |
| Paying customers | 2 | 5 of first 8 converted to paid in 30 days, now 7 in the narrow who (experiment_log EXP-03) |
| LOF tested by behavior | 2 | Conversion + board-free Mondays test the leap by behaviour, not intent (experiment_log EXP-03/EXP-04) |
| Built to learn | 3 | Each test pre-registered a behavioural threshold before running (experiment_log all rows) |
| Instrumented | 2 | Retention measured as a board-free Monday streak per farm; per-view open-time still being wired (experiment_log EXP-04; hypotheses H3) |

**Gate:** all ≥ 2 and no 0s? **[x] yes  [ ] no** → advanced to Stage 06.

---

## Stage 04 — Value Hypothesis

| Dimension | Score (0–3) | Cited evidence (artifact + ref) |
|---|---|---|
| What | 3 | "Daily per-worker cut list by 5am", buildable in 3-6mo, with the weekly planner explicitly excluded (decision_dossier.md; hypotheses H4) |
| Who | 3 | Narrow and nameable: mid-market multi-site leafy-green, 20-80 staff, Argus/Priva (interviews.csv rows 6-15) |
| How | 2 | Monthly subscription, charged from day one; no free tier (experiment_log EXP-03) |
| Leap of faith | 3 | One behavioural assumption isolated and a direct test designed (lof_ledger.md) |
| What's NOT in v1 | 2 | Explicit exclusions: weekly planning, climate-control integration, non-leafy crops (founder-state who.excluded analog; lof_ledger.md) |
| Stress-tested | 2 | Survived the failed single-site concept test and a deliberate who-pivot before commitment (experiment_log EXP-00) |

**Gate:** all ≥ 2 and no 0s? **[x] yes  [ ] no** → advanced to Stage 05.

---

## Stage 03 — Problem–Solution Fit

| Dimension | Score (0–3) | Cited evidence (artifact + ref) |
|---|---|---|
| Problem statement | 3 | Every line evidenced as dawn behaviour with a deadline (interviews.csv rows 6, 11; decision_dossier.md) |
| One pain | 3 | One sharp pain — the 5am scramble — quantified by frequency (daily) and magnitude (missed retail cutoff, composted rack) (interviews.csv rows 6, 8) |
| Painkiller not vitamin | 2 | Clear painkiller: removes a daily failure-prone manual task (interviews.csv rows 6, 9, 15) |
| Unit economics | 2 | Monthly subscription against a recurring labour cost; LTV/CAC > 3 plausible at scale, payback not yet proven (pmf_dashboard.md) |
| Concept-test commitments | 2 | 6 of 9 booked follow-ups, 4 sent real crop schedules — behavioural, not compliments (experiment_log EXP-01) |
| Leap of faith | 3 | One behavioural assumption named with a direct test (lof_ledger.md) |

**Gate:** all ≥ 2 and no 0s? **[x] yes  [ ] no** → advanced to Stage 04.

---

## Stage 02 — Customer Discovery

| Dimension | Score (0–3) | Cited evidence (artifact + ref) |
|---|---|---|
| Narrow who | 3 | 10 real in-segment names listed (interviews.csv rows 6-15) |
| Desperation markers | 2 | 5 of 15 score 3-4 on the four markers, clustered in the narrow who (interviews.csv rows 7, 11, 14 = 4; rows 6, 9, 15 = 3) |
| Workaround evidence | 3 | Multiple independently built: 9-tab spreadsheet, laminated master sheet, nightly self-emailed sheet, photographed board (interviews.csv rows 7, 9, 14, 15) |
| Recurrence | 2 | The 5am scramble came up unprompted and emotionally charged across the segment (interviews.csv rows 6, 11) |
| Mom Test discipline | 2 | Scored on past behaviour and money spent, not "would you use it" (interviews.csv past_behavior_quote column); collapsed H8 enforces this |
| Sample depth | 2 | 15 interviews with synthesis; below the 30+ that would score a 3 (interviews.csv rows 1-15) |

**Gate:** all ≥ 2 and no 0s? **[x] yes  [ ] no** → advanced to Stage 03 (after the who-pivot inside this stage; see lof_ledger.md and experiment_log EXP-00).

---

_(Stages 00-01 cleared earlier; blocks omitted here for brevity. Newest block stays on top.
Don't delete old blocks — they become the decision_dossier.md trail.)_
