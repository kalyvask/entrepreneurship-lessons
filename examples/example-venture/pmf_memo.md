# Croplane — PMF Memo

**Date:** 2026-05-28  **Stage:** approaching PMF  **Author:** worked example

> Capstone for this worked example. Follows the shape of `templates/pmf_memo.md`. Written
> honestly: approaching PMF in one narrow segment, with the evidence and the gaps both stated.
> No happy ears. Every claim cites a workspace artifact or is flagged as an open hypothesis.

---

### 1. The insight (one paragraph)

> Because indoor leafy-green farms have gone multi-site while their software stack (Argus,
> Priva) only runs the growing environment, it is now necessary to schedule the daily harvest
> across sites and crews — a job that sits in the gap between "the crop is ready" and "this
> person cuts that bed". Incumbents can't pursue it because their products are built around
> climate and the plant, not the labour; crew-level scheduling sits outside their
> resources, processes and values (RPV), so it is a job they will not prioritise.

Why now, with evidence:

> Mid-market CEA operators are running 2-4 sites with a single ops lead holding the harvest
> plan by hand; the coordination cost only appears at multi-site scale (interviews.csv rows
> 6-15). At single-site scale it doesn't exist yet (rows 1-5).

What's non-consensus about it (who would disagree, and why they're wrong):

> CEA software vendors assume the climate system is the center of gravity and harvest "falls
> out of" it. For tech-forward single-site farms that's true (interviews.csv rows 1, 3). For
> mid-market multi-site farms it is false: the schedule is redrawn by hand at 5am every day.

### 2. The value hypothesis

- **What:** a daily per-worker harvest cut list, ready before 5am; weekly planning explicitly excluded.
- **Who:** mid-market leafy-green CEA farms, 20-80 staff, 2+ sites, on Argus/Priva, scheduling by hand *(can name 10: interviews.csv rows 6-15)*.
- **How:** monthly subscription, charged from day one, sold direct to the ops lead.
- **Leap of faith:** they will pay monthly and run Monday harvest off Croplane instead of the whiteboard, because the 5am scramble is a recurring labour cost they already absorb by hand.

### 3. The customer & the desperation

The desperate customer is the multi-site ops lead. Evidence she is desperate, not just needy:

| Evidence | Detail |
|---|---|
| Workarounds they've built | 9-tab spreadsheet computing cut order (row 7); laminated master sheet rewritten daily (row 9); spreadsheet self-emailed nightly to have on a phone at 5am (row 14); photographed colour-coded board (row 15) |
| Money/time already spent on the problem | $400 to an Upwork freelancer to clean up the spreadsheet (row 7); paid a generic workforce app for two months, then churned because it knew shifts but not crops (row 10) |
| Pain raised unprompted | The 5am scramble, the missed retail cutoff (row 6), the composted rack (row 8), the double-cut beds (row 15) — all volunteered |
| "When can I have it?" urgency | 6 of 9 booked a follow-up unprompted at concept test; 3 of 4 asked to keep using a clickable facade (experiment_log EXP-01, EXP-02) |

Named design partners / early customers: L. Tran, P. Castellano, K. Nielsen, G. Santos, N. Haddad, B. Fischer and one more, all in the narrow who (interviews.csv rows 6-15).

### 4. Validation to date

| Test | Method | Result | What it proved |
|---|---|---|---|
| Concept | One-page mockup to 9 in-segment ops leads; pre-registered >=5 book, >=3 send data | 6 booked, 4 sent real crop schedules in 72h | The cut-list concept pulls costly action in the narrow who (EXP-01) |
| Implementation | Knapp 5-day sprint; clickable facade on one farm's real data, 4 ops leads | 3 of 4 ran a live Monday unaided and asked to keep it; the 4th hit stale data | The design carries a real Monday; daily re-sync is load-bearing (EXP-02) |
| MVP | Real paid product to first 8 invited farms; pre-registered >=4 convert in 30 days | 5 of 8 paid within 30 days, zero 30-day churn | Willingness-to-pay verified by behaviour (EXP-03) |

Has the leap of faith been tested? **Still open** — by what specific behavior:

> Willingness-to-pay is confirmed (5 of 8 paid in 30 days). The durable half — running Monday
> off Croplane with the whiteboard down for good — is confirmed for 6 of 7 over 4 weeks but
> fragile: 1 reverted during a staff transition (experiment_log EXP-04). So: payment verified,
> habit not yet durable. The leap as a whole stays open.

### 5. Metrics (product in market)

| Metric | Value | Read |
|---|---|---|
| Paying customers in narrow who | 7 | up from 5 at Stage 06 entry; small but all in-segment |
| Sean Ellis "very disappointed" % | 38% (n=8) | below the 40 bar; climbing from 26% |
| Retention curve (paying, wk 12) | 6 of 7 active; flattening above zero | right shape, only 8 weeks flat |
| Organic % of new customers | 35% | climbing from 0%; thin (4 recent logos) |
| The tells | 2 of 3: unasked referrals, shrinking sales cycle | pricing power not yet tested |

### 6. The surprise

> The over-performing slice was the segment we almost skipped because it was *harder* to reach.
> The tech-forward single-site farms we expected to be the beachhead had already automated the
> job; the bleed was in mid-market multi-site farms on legacy climate control, where one person
> redraws the plan at 5am. The thing worth doubling down on: accounts where a crew lead (not
> just the ops lead) opens the plan retain hardest — second-seat usage looks like the real
> stickiness signal (hypotheses H7). We are now building toward it deliberately.

### 7. The decision / the ask

- **Verdict:** Approaching — enhancing the good. Hold the narrow who; deepen retention before widening or declaring PMF.
- **Most important next action:** ship and pilot a crew-lead (second-seat) view at 2 farms; treat any single-seat account as at-risk on the dashboard (hypotheses H7).
- **What would change the verdict:** Sean Ellis crossing 40% on a larger n than 8, retention staying flat through a dormant season, and second-seat usage appearing — that would be PMF. A second farm reverting to the whiteboard in a normal week would push it the other way.
- **The ask (if sharing externally):** warm intros to mid-market multi-site leafy-green operators on Argus/Priva; not single-site, not non-leafy.

### 8. Honest risks

The things most likely to be wrong (the pre-mortem — what kills this in 2 years):

- The narrow who may be too small to build a venture on (a few thousand farms worldwide). Holding the line is right for now, but the TAM ceiling is a real open question.
- Value may be trapped in one role. 5 of 7 accounts are single-seat; if the ops lead leaves, the account may churn (hypotheses H7; founder-state risks).
- A climate-control vendor (Argus/Priva) or an ERP could bundle daily scheduling and foreclose the wedge. The defense is staying narrow and fast on a job they don't prioritise — which only works while we are faster than they are bothered.
