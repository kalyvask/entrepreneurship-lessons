# Example Venture — Croplane

A filled, end-to-end worked example of the venture journey. Every file here mirrors the
[`scaffold/`](../../scaffold/) structure exactly — same fields, same columns, same 0-3 scales
— only the content is populated. Read it alongside
[`playbooks/validation_sequence.md`](../../playbooks/validation_sequence.md), which threads the
same CEA venture stage to stage.

**The venture in one line:** Croplane is daily-harvest scheduling that turns a CEA farm's crop
plan into per-worker cut assignments by 5am, for mid-market multi-site leafy-green farms
(20-80 staff, running Argus/Priva climate control).

**Where it is:** Stage 06, approaching PMF, *not there yet*. 7 paying customers in the narrow
who. Sean Ellis 38% and climbing (was 26%). Retention flattening above zero. Organic ~35% and
rising. Willingness-to-pay is verified by behaviour; retention depth is the open gap.

## Stage map (00 → 07)

| Stage | What happened | Where the evidence lives |
|---|---|---|
| 00 — Prepared Mind | Two seasons working harvest on an indoor leafy-green farm; crews stood idle each morning waiting to be told what to cut; the plan lived in one grower's head | `founder-state.yaml` history (2024-09-02); `decision_dossier.md` Insight |
| 01 — Insight & Idea | The harvest schedule sits in the gap between "crop is ready" and "this person cuts that bed"; the climate stack ignores labour | `decision_dossier.md` Insight; `pmf_memo.md` section 1 |
| 02 — Customer Discovery | 15 interviews. Real workarounds and prior spend, but desperation split hard by farm size. **Who-pivot:** dropped tech-forward single-site farms (easy to reach, no live pain), narrowed to mid-market multi-site leafy-green | `interviews.csv` rows 1-15; `lof_ledger.md` history; `founder-state.yaml` history (2025-01-20 who-pivot); `rubric_scores.md` Stage 02 |
| 03 — Problem–Solution Fit | Found the workaround: whiteboard redrawn at 5am, 9-tab spreadsheets, 5am texts. People already paying a daily cost | `interviews.csv` rows 6, 9, 11, 14, 15; `rubric_scores.md` Stage 03 |
| 04 — Value Hypothesis | One behavioural leap isolated; weekly-planner scope cut before any build | `lof_ledger.md`; `decision_dossier.md` Value hypothesis; `rubric_scores.md` Stage 04 |
| 05 — MVP Build | Concept test (6 of 9 booked, 4 sent data) → Knapp sprint (3 of 4 ran a live Monday unaided) → MVP (5 of 8 paid in 30 days) | `experiment_log.md` EXP-01/EXP-02/EXP-03; `rubric_scores.md` Stage 05 |
| 06 — PMF Measurement | First paid logos, now 7. Sean Ellis 26% → 38%. Retention flattening; 1 revert under a staff transition. Approaching, not at, PMF | `pmf_dashboard.md`; `experiment_log.md` EXP-04; `rubric_scores.md` Stage 06; `pmf_memo.md` |
| 07 — Pivot or Persevere | Not reached as an exit. The earlier who-pivot is logged as a Stage-07-type decision; the capstone memo states the PMF gap honestly rather than declaring fit | `decision_dossier.md` Pivots; `pmf_memo.md` sections 7-8 |

## The files

Same set as `scaffold/`, all filled:

| File | What it holds here |
|---|---|
| `founder-state.yaml` | Current stage 06; gate scores 0-3; append-only history showing 00 → … → who-pivot → 06 |
| `lof_ledger.md` | The original leap, the refuted single-site leap, and the current leap (status: testing) |
| `interviews.csv` | 15 rows scored on the four 0/1 desperation markers; the workaround signal (rows 7, 14) |
| `hypotheses.md` | Strengthened (H1-H3) and collapsed (H0, H4, H8) hypotheses, confidence 0-1 |
| `experiment_log.md` | Concept (EXP-00 failed, EXP-01 passed) → Knapp implementation (EXP-02) → MVP (EXP-03, EXP-04), each pre-registered |
| `rubric_scores.md` | One scored 0-3 block per stage 02-06, each 2-3 citing a specific artifact |
| `pmf_dashboard.md` | Approaching-PMF numbers in the narrow who; the vanity section left intact |
| `decision_dossier.md` | Insight → problem → value hypothesis → validation → the pivot decision |
| `pmf_memo.md` | The capstone, written honestly against `templates/pmf_memo.md` |
| `thesis_ledger.md` | The endgame artifact: Croplane's learnings logged with rule-of-three flags (two promoted, two n=1 candidates), feeding the PMF-insights / style-memo / value-hypothesis-stance synthesis. Per founder in practice — shown here so the example runs end to end |

## What this example is meant to show

- **Iterate the who, not the what.** The product idea barely changed; the customer was wrong.
  The pivot (Stage 02) was driven by a *failed pre-registered test* (`experiment_log.md`
  EXP-00), not a hunch.
- **Behaviour over opinions.** Every claim cites a workaround built, a follow-up booked, a
  schedule sent, a dollar paid, or a whiteboard taken down. Collapsed hypothesis H8 is kept on
  purpose: stated intent did not predict adoption.
- **Narrow, then narrower.** "Indoor farms" → "indoor vertical farms" → "mid-market multi-site
  leafy-green, 20-80 staff, Argus/Priva". Each cut was earned by evidence.
- **Honest, not triumphant.** Numbers are small and the dashboard keeps its vanity row to show
  the trap. Sean Ellis is reported at 38%, not rounded up to 40. The memo's verdict is
  "approaching", and section 8 lists what could still kill it.

## When guidance conflicts

This example follows the repo rule: when sources disagree, the **PMF learnings win** —
desperation over need, behaviour over opinions, the narrow *who*, the rate of learning over
the rate of shipping. Score the evidence, not the hope.
