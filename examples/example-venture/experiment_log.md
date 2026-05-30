# Experiment Log

Every test you run — concept, implementation, MVP — with its pass threshold written down
**before** you run it. Pre-registration is what stops you from rationalising any result as
success. The cheapest test that could disconfirm the leap of faith is the best test.

> FILLED EXAMPLE (Croplane). Note EXP-00: a pre-registered concept test that FAILED. Keeping
> it is the point — that clean failure is what earned the right to pivot the who deliberately,
> instead of on a hunch. The sequence then runs concept (EXP-01) to implementation/Knapp
> sprint (EXP-02) to MVP (EXP-03, EXP-04).

| Date | Stage | Type | What you ran | Pre-registered pass threshold | Result (behaviour) | Pass? | Decision |
|---|---|---|---|---|---|---|---|
| 2024-12-18 | 02 | concept | One-page mockup of an auto-generated daily cut list, shown to 5 tech-forward single-site farms | >=3 of 5 book a follow-up unprompted AND >=2 send a real crop schedule | 1 of 5 booked a follow-up; 0 sent a schedule; 2 said the cut list was "already handled" | no | pivot-who: kill the tech-forward single-site segment; narrow to mid-market multi-site (lof_ledger.md) |
| 2025-03-24 | 03 | concept | Same one-page mockup, shown to 9 mid-market multi-site ops leads | >=5 of 9 book a follow-up unprompted AND >=3 send a real crop schedule to seed it | 6 of 9 booked a follow-up; 4 sent a real crop schedule within 72h | yes | persevere: advance to an implementation test seeded with real data |
| 2025-05-12 | 05 | implementation | Knapp 5-day sprint: clickable Figma facade of the daily-harvest flow, seeded with one farm's real crop schedule, tested with 4 ops leads | >=3 of 4 run a live Monday off the facade with no help AND ask to keep using it | 3 of 4 ran the full Monday unaided; the 4th hit stale germination data, needed a manual fix, still asked to keep it | yes | persevere: build the MVP; make daily re-sync the first priority (the stale-data failure mode) |
| 2025-08-11 | 06 | MVP | Real product, paid, offered to the first 8 invited in-segment farms | >=4 of 8 convert to a paid monthly subscription within 30 days | 5 of 8 converted to paid within 30 days (2 more later); zero 30-day churn | yes | persevere: enter Stage 06. Willingness-to-pay verified by behaviour, not a "yes" (lof_ledger.md) |
| 2026-04-06 | 06 | MVP | Retention test: track whether paying farms run 4 consecutive Mondays with the whiteboard physically down | >=5 of 7 farms hit a 4-week board-free streak | 6 of 7 hit the streak; 1 reverted to the board during a staff transition week | partial | persevere but do not declare PMF: retention is real yet fragile at staff transitions; prioritise the second-seat (crew-lead) view (hypotheses H7) |

## Notes

- **Type** runs cheapest-first: concept test (days) → implementation test (~1 week) →
  MVP test (1–3 months). Don't skip to MVP; one big test confounds too many variables.
- **Result** records what people *did* (paid, booked, signed, churned), not what they said.
- A single weak result is not a kill — usually the *who* or the messaging is wrong before
  the concept is. Run more than one before concluding.
- Each row that verifies or refutes the leap of faith updates `lof_ledger.md`.
- Discipline check: after EXP-03 came in at 5 of 8, it was tempting to retro-lower the bar to
  3 of 8 to claim a cleaner win earlier. The bar was left at 4 of 8 as pre-registered. Moving
  goalposts mid-experiment poisons the read.
