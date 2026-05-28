# Retention Dashboard — Template

Used in [Stage 06 — PMF Measurement](../stages/06_pmf_measurement.md). Retention is one of the two load-bearing PMF signals (the other is the Sean Ellis test). This template structures the cohort-retention analysis that tells you whether your curve **flattens above zero** (PMF) or **asymptotes to zero** (no PMF, regardless of revenue).

See [`frameworks/pmf_measurement.md`](../frameworks/pmf_measurement.md) for the interpretation.

---

## Project: ___________________________

## Date: ___________________________

## Narrow who segment: ___________________________

---

## 1. Define your retention event

What counts as "retained" for this product? Be specific — the wrong event makes the whole analysis meaningless.

- SaaS: ___________ (e.g., "logged in and performed core action in the week")
- Consumer: ___________ (e.g., "opened app and completed key action")
- Marketplace: ___________ (e.g., "transacted")

**Retention event:** ___________________________________________________

**Cohort window:** [ ] Weekly  [ ] Monthly

---

## 2. The cohort grid

Rows = acquisition cohort (when they signed up). Columns = periods since acquisition. Cell = % of cohort still performing the retention event.

| Cohort | Period 0 | 1 | 2 | 4 | 8 | 12 | 24 |
|---|---|---|---|---|---|---|---|
| [Month 1] | 100% | | | | | | |
| [Month 2] | 100% | | | | | | |
| [Month 3] | 100% | | | | | | |
| [Month 4] | 100% | | | | | | |
| [Month 5] | 100% | | | | | | |

**Do this for PAYING customers specifically** (a separate grid). Free-user retention is much weaker signal.

---

## 3. The shape diagnosis

Plot the curves. Which pattern?

- [ ] **Flattens above zero** — strong PMF signal. The plateau is your sticky core. Note the plateau level: _____%
- [ ] **Asymptotes to zero** — NO PMF. Every cohort eventually churns out. Revenue can't save this.
- [ ] **Improving cohort-over-cohort** — approaching PMF. Newer cohorts retain better. Keep going. (The product is getting better for your who.)
- [ ] **Declining cohort-over-cohort** — concerning. Newer cohorts retain worse — usually means you've broadened the who and diluted desperation.

**Plateau level (paying, week 12):** _____%

Rough health benchmarks (thresholds, not targets — the *shape* matters more):
- SaaS: 30%+ active at week 12 for a paying cohort = healthy
- Consumer: 25%+ at week 4 = healthy
- Marketplace: GMV/cohort flat or rising at week 12 = healthy

---

## 4. The over-performing slice

Is there a sub-segment retaining at 2–5× the average? (See "savor the surprise" in [Stage 06](../stages/06_pmf_measurement.md).)

**The slice:** _________________________________________________________

**What's distinctive about them** (segment, use case, acquisition channel, company size): ___________________________________________________________

**Action:** find more like them; serve them deeper. (Enhance the good, don't fix the bad.)

---

## 5. Companion metrics (for the full PMF picture)

| Metric | This period | Trend |
|---|---|---|
| Sean Ellis "very disappointed" % (narrow who) | | |
| Organic % of new customers | | |
| Net revenue retention | | |
| Logo retention | | |

(Retention alone isn't PMF — combine with the Sean Ellis test and organic acquisition. See [`playbooks/pmf_assessment.md`](../playbooks/pmf_assessment.md).)

---

## 6. Verdict

- [ ] Curve flattens above zero AND Sean Ellis ≥ 40% in narrow who → **PMF**
- [ ] Curve improving, Sean Ellis climbing → **approaching — keep going, enhance the good**
- [ ] Curve asymptotes to zero → **no PMF — see [Stage 07](../stages/07_pivot_or_persevere.md)**

**Most important action this quarter:** ___________________________________

---

See [`frameworks/pmf_measurement.md`](../frameworks/pmf_measurement.md) and [`playbooks/pmf_assessment.md`](../playbooks/pmf_assessment.md).
