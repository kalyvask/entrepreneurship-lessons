# Leap-of-Faith Ledger

The leap of faith is the *one* behavioral assumption your business depends on. If it is
false, nothing else matters. It is the thread that runs through every stage — discovery
tests whether it's plausible, the MVP tests whether it's true, a pivot changes it
deliberately. Track it here, in one place, over time.

Rules:
- **One** leap of faith at a time. If you have five, you can't interpret any test.
- It is **behavioral**, not technical. "Can we build it" is engineering risk, not a leap of faith.
- A status of `verified` or `refuted` requires a row in `experiment_log.md` (behavior, not opinion).

> FILLED EXAMPLE (Croplane). The history below shows the original leap, the who-pivot that
> killed it, and the current leap now under test. Note: the current leap is `testing`, not
> `verified` — willingness-to-pay is verified by behaviour, but a paid logo is not yet a kept habit.

## Current leap of faith

> Mid-market multi-site leafy-green farms will pay monthly and run Monday harvest off
> Croplane instead of the whiteboard, because the 5am scheduling scramble is a recurring
> labour cost they already absorb by hand.

- **Narrow who it applies to:** mid-market leafy-green CEA farms, 20-80 staff, 2+ sites, on Argus/Priva, scheduling by hand (interviews.csv rows 6-15).
- **Test running against it:** retention as a board-free Monday streak (`experiment_log.md` EXP-04); preceded by the paid-conversion test (EXP-03).
- **Status:** `testing`
- **What would verify it:** the same farms run consecutive board-free Mondays AND a second seat (crew leads) opens the plan directly — pre-registered as >=5 of 7 with a 4-week board-free streak and rising second-seat usage.
- **What would refute it:** farms keep paying but quietly revert to the whiteboard, or usage stays trapped in one person who, if she leaves, takes the account with her.

## History

Append a row whenever the leap of faith changes (a pivot changes the *who*/*how*; a restart
changes the *what*). Don't delete past rows — the history is the protection against
pretending you didn't pivot.

| Date | Leap of faith | Who | Status | Evidence (experiment_log ref) | Why it changed |
|---|---|---|---|---|---|
| 2024-10 | Indoor farms will adopt software to schedule harvest because the plan lives in one person's head and crews wait on it | Indoor vertical farms (all sizes) | refuted | EXP-00 | Too broad. Spend behaviour split hard by farm size (interviews.csv rows 1-15). The "who" was hiding two opposite segments; split it |
| 2024-12 | Tech-forward single-site vertical farms will pay for harvest scheduling because they are software-friendly and easy to reach | Tech-forward single-site vertical farms | refuted | EXP-00 | Concept test failed: 1 of 5 booked a follow-up, 0 sent a schedule. 3 of 5 had already automated the cut list; 2 were under 12 staff with no coordination cost (interviews.csv rows 1-5). Reachability was our convenience, not their pain. Drove the who-pivot |
| 2025-01 | Mid-market multi-site leafy-green farms already pay a manual cost to schedule harvest and will switch that working habit onto a tool | Mid-market multi-site leafy-green, 20-80 staff, Argus/Priva | testing | EXP-01, EXP-02, EXP-03, EXP-04 | Workaround found at 7 of 8 (interviews.csv rows 6-15); 6 of 9 booked follow-ups and 4 sent real data at concept test; 5 of 8 converted to paid. WTP verified; retention depth still being established |

## Graveyard note (kept on purpose)

The dead leap above (tech-forward single-site) is the most useful row in this file. We chased
the slice that was easy to talk to, not the slice that was bleeding. "Easy to reach" and
"desperate" are different axes. The pain lives where coordination cost is high: multiple sites,
multiple crews, a legacy climate stack that schedules the environment but not the labour.

A second, smaller leap also died on 2025-03: "farms will plan harvest a week ahead and value
an editable weekly view." Nobody used the weekly view; farms re-plan every morning against
actual germination, weather and no-shows. The job is daily, not weekly. We cut the weekly
planner (hypotheses.md H4) and the product got sharper.
