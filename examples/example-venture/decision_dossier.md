# Decision Dossier

A running, exportable record of the decisions you can actually defend. It is assembled as
you clear gates — not written at the end. When a co-founder, advisor, or investor asks
"why this?", this is the document you hand them. The capstone is the PMF memo
(`/ent-pmf-memo`); this dossier is everything that leads to it.

Each entry: the decision, the date, and the **evidence** it rests on (linked into this
workspace). No evidence link, no entry.

> FILLED EXAMPLE (Croplane). The spine is the who-pivot in the Pivots section: the product
> idea barely changed; the customer was wrong, and "easy to reach" had disguised it.

---

## Insight (Stage 01)
- **Decision:** Build daily-harvest scheduling for CEA farms — the job that sits in the gap between "the crop is ready" (which the climate stack knows) and "this person cuts that bed" (which nobody owns). The climate stack runs the environment and ignores labour.
- **Evidence:** Two seasons working harvest firsthand; crews stood idle each morning waiting on a plan held in one grower's head (hypotheses.md H1; later confirmed across interviews.csv rows 6-15).
- **Date:** 2024-10-14

## Problem (Stage 02–03)
- **The desperate who:** mid-market multi-site leafy-green CEA farms, 20-80 staff, on Argus/Priva, scheduling harvest by hand.
- **The one pain:** the 5am scramble — one overloaded ops lead redraws a whiteboard against actual germination and no-shows and texts cut assignments to crew leads before they clock in.
- **Evidence of desperation:** workarounds built independently (9-tab spreadsheet, laminated master sheet, nightly self-emailed sheet), money already spent (a $400 freelancer, a churned workforce app), and concrete failure costs (missed retail cutoff, composted rack, double-cut beds) (`interviews.csv` rows 6, 7, 8, 9, 10, 14, 15).
- **Date:** 2025-02-17

## Value hypothesis (Stage 04)
- **What / Who / How:** What — a daily per-worker cut list ready before 5am (weekly planning explicitly excluded). Who — the narrow segment above. How — monthly subscription, charged from day one, sold direct to the ops lead.
- **Leap of faith:** these farms will pay monthly and run Monday harvest off Croplane instead of the whiteboard, because the 5am scramble is a recurring labour cost they already absorb by hand (`lof_ledger.md`).
- **Date:** 2025-04-21

## Validation (Stage 05–06)
- **Tests run + results:** concept test 6 of 9 booked follow-ups / 4 sent real data (EXP-01); Knapp implementation sprint 3 of 4 ran a live Monday unaided (EXP-02); MVP 5 of 8 paid within 30 days, zero 30-day churn (EXP-03); retention 6 of 7 ran 4 board-free Mondays, 1 reverted (EXP-04) (`experiment_log.md`).
- **PMF read:** approaching PMF, not at it. Sean Ellis 38% and climbing (bar 40%), retention flattening above zero, organic ~35% rising, pricing power untested (`pmf_dashboard.md`).
- **Date:** 2026-05-28

## Pivots / persevere decisions (Stage 07)
- **Decision + type (who / how / restart / persevere):** WHO-PIVOT (not a restart). Dropped tech-forward single-site vertical farms; narrowed to mid-market multi-site leafy-green. Kept the core "what" (daily cut list) and the discipline of pre-registering a behavioural threshold per test.
- **Why, from the data:** a pre-registered concept test on the single-site slice failed — 1 of 5 booked a follow-up, 0 sent a schedule; 3 of 5 had already automated the cut list and 2 were under 12 staff with no coordination cost. Desperation lived in the harder-to-reach multi-site segment instead (`experiment_log.md` EXP-00; `interviews.csv` rows 1-5 vs 6-15; `lof_ledger.md`).
- **Date:** 2025-01-20

---

_Newest decisions at the bottom of each section. This file is safe to export and share;
keep `interviews.csv` and raw notes private if they contain names._
