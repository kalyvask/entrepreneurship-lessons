# Hypothesis Tracker

Make your beliefs explicit so the evidence can move them. Review weekly. Some hypotheses
gain weight; others collapse. Both are progress. The most important column is the last one
— pre-register what would change your mind *before* you go looking.

> FILLED EXAMPLE (Croplane). Some hypotheses strengthened (H1, H2, H3), some collapsed
> (H0, H4, H8 — kept on purpose). Confidence is 0-1. Behaviour outweighs opinions throughout.

| Hypothesis | Stated by | Supporting evidence | Contradicting evidence | Confidence (0-1) | What would change my mind |
|---|---|---|---|---|---|
| H1: Mid-market multi-site leafy-green farms scheduling by hand already run a costly daily workaround | founder, after pivot | 7 of 8 in-segment farms had a live workaround: whiteboard, 9-tab sheet, nightly self-emailed sheet (interviews.csv rows 6-15) | 1 farm (H. Park, row 12) had a sheet the crew ignored — partly absorbed by the manager | 0.9 | Finding a sizeable in-segment cohort with no workaround and no felt cost |
| H2: These farms will pay monthly for a working daily cut list | founder | 7 paying monthly; 5 of first 8 converted within 30 days before any annual discount (experiment_log EXP-03; pmf_dashboard.md) | none yet inside the narrow who | 0.8 | A price increase that collapses close rate, showing the willingness was thin |
| H3: The job they value is the per-worker cut list ready before 5am | discovery synthesis | 6 of 7 open the morning cut list on their phone before crews arrive; planning views go largely unopened (experiment_log EXP-02 notes) | one farm uses it mid-morning to re-balance crews, not at 5am | 0.8 | Usage clustering away from the dawn window once instrumented |
| H5: If the tool is load-bearing, farms run consecutive Mondays with the whiteboard down | founder | 6 of 7 ran their last 4 consecutive Mondays board-free (experiment_log EXP-04) | 1 farm reverted to the board during a staff transition week | 0.6 | A second or third farm reverting under normal (non-transition) weeks |
| H6: Value inside the segment shows up as unprompted peer referrals | founder | 2 of last 4 logos were inbound referrals from existing customers (pmf_dashboard.md organic 35%) | first 5 logos were all outbound; referral base is thin (4 recent logos) | 0.5 | Organic share falling back under 30% across the next 6 logos |
| H7: Value is not trapped in one person — a second seat (crew leads) will open the plan | founder | 2 of 7 accounts have a crew lead opening the plan directly | 5 of 7 are single-seat (only the ops lead logs in) | 0.4 | A pilot crew-lead view at 2 farms failing to produce any second-seat weekly active |

## Collapsed hypotheses (kept on purpose)

| Hypothesis | Stated by | Why it collapsed (the behaviour that wasn't there) | Lesson |
|---|---|---|---|
| H0: Tech-forward single-site vertical farms are the beachhead because they adopt software readily | founder, pre-pivot | They didn't pay, ask a price, or build a workaround. 3 of 5 had already automated the cut list; 2 were under 12 staff (interviews.csv rows 1-5; experiment_log EXP-00) | "Easy to reach / software-friendly" is not "desperate". Narrow toward the bleed. This drove the who-pivot (lof_ledger.md) |
| H4: Farms will plan harvest a week ahead and value an editable weekly view | founder | The weekly view went unused; farms re-plan every morning against germination, weather and no-shows. A week-ahead plan was stale by Tuesday | The job is daily, not weekly. Cutting the weekly planner sharpened the product |
| H8: Stated intent predicts adoption — farms that said "yes, I'd use this" will become users | founder | Of the 6 who said yes most enthusiastically at concept test, only 3 sent a real crop schedule when asked | Score behaviour (sent data, booked time, paid), never the "yes". Updated discovery to ignore opinion answers |

## Notes

- A **pattern** = 3+ independent sources, unprompted. A single enthusiastic person is an
  **anecdote** — interesting, not yet evidence.
- Weight behavior (workarounds built, money spent) far above opinions (compliments, "I would").
- Tensions between hypotheses are signal, not noise. The tension between H2 (they pay) and H7
  (value may be trapped in one seat) is exactly where the PMF risk lives — probe it before scaling.
