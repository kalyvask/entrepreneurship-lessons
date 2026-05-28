# PMF Survey — Sean Ellis Template

Use this with active users in your narrow *who* segment. N ≥ 50 for meaningful signal.

---

## Survey setup

**When to send:** to users who have used the product **at least 3 times** in the past 4 weeks.
**Tool:** Typeform, Google Forms, intercom, in-app, email — any.
**Length:** 5 questions, < 3 minutes.
**Audience:** ONLY active users in your narrow *who*. Do not send to broader base; the signal washes out.

---

## The questions

### Q1 — The core Sean Ellis question

**How would you feel if you could no longer use [product name]?**

- [ ] Very disappointed
- [ ] Somewhat disappointed
- [ ] Not disappointed (it isn't really that useful)
- [ ] N/A — I no longer use [product name]

---

### Q2 — Why? (Open-ended, all respondents)

**Whatever you answered above — could you say a few words about why?**

[Open text]

This is the most important answer. Mine the comments from the "Very disappointed" cohort especially. Their reasons should map to desperation markers.

---

### Q3 — Who would benefit most? (Open-ended)

**Who else do you think would benefit most from [product name]?**

[Open text]

Useful for:
- Refining the narrow *who* (do they describe your hypothesized segment, or a different one?)
- Identifying referral candidates
- Discovering adjacent segments you didn't expect

---

### Q4 — What's the main benefit? (Open-ended)

**What's the main benefit you get from [product name]?**

[Open text]

You're looking for **specific language** that maps to the value hypothesis. If respondents are describing benefits that aren't in your hypothesis, that's signal (could be enhancing, or could mean wrong hypothesis).

---

### Q5 — Improvements (Open-ended)

**How can we improve [product name] for you?**

[Open text]

Take these with a grain of salt — see [`frameworks/the_mom_test.md`](../frameworks/the_mom_test.md) on the unreliability of feature requests. But: if multiple "very disappointed" users describe the same missing piece, that's signal.

---

## Analysis

### The headline number

Of users who answered Q1 (not the "no longer use" cohort):

```
"Very disappointed" % = (very disappointed responses) / (total responses excluding N/A)
```

**Benchmarks:**
- 40%+ — PMF or close. Strong signal.
- 25–40% — approaching. Investigate the segment carefully.
- 10–25% — common pre-PMF range. Need to narrow further.
- < 10% — significant work to do.

### Segmentation

Cut the number by:
- The narrow *who* segment specifically (vs broader)
- Customer cohort (when they signed up)
- Usage frequency (high vs low usage among active)
- Channel of acquisition (organic vs paid)

You're looking for **the slice with the highest "very disappointed" %.** That's your over-performing segment — see [Stage 06](../stages/06_pmf_measurement.md) on "savor the surprise."

### The comments

For the "Very disappointed" cohort specifically:

- What's the common job they describe?
- What's the common pain if the product disappeared?
- Do their reasons map to the desperation markers?
- What language do they use to describe the benefit?

**Useful trick:** use this language verbatim in landing pages, sales calls, and marketing. The "very disappointed" cohort is telling you what to say to find more of them.

---

## What to do with the result

| Result | Action |
|---|---|
| > 40% | You have PMF. Move from search to scale. |
| 30–40% in narrow who | Approaching PMF. Enhance the good. Find more of these customers. |
| < 30% broadly but a sub-segment > 40% | The sub-segment is where PMF is. Pivot the *who* tighter. |
| < 30% across all segments, no over-performing slice | No PMF. See [Stage 07](../stages/07_pivot_or_persevere.md). |

---

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Surveying everyone, not just active users | "Very disappointed" % gets diluted by tourists |
| N < 30 | Individual responses dominate; not meaningful |
| Only the number, no comment box analysis | Misses the *why* — half the signal |
| Treating Q5 (improvements) as a roadmap | Compliments are zero signal; feature requests need filtering |
| Re-running after every product change | Run quarterly; let the data accumulate |
| Reporting blended results | Cut by segment, cohort, channel |
| Comparing to industry benchmark instead of trend | Your trajectory matters more than the absolute number |

---

## When to run it

- Q3 of MVP testing (you have enough users by then)
- Every quarter pre-PMF
- After any major product change
- After narrowing the *who* (to verify the change worked)

---

## Source

Created by Sean Ellis, growth advisor at Dropbox, Eventbrite, LogMeIn. The 40% benchmark is folkloric — there's no statistical magic in it — but the principle (high concentration of desperate users = PMF approaching) is robust.

See [`frameworks/pmf_measurement.md`](../frameworks/pmf_measurement.md) for fuller PMF measurement discipline.
See [`playbooks/pmf_assessment.md`](../playbooks/pmf_assessment.md) for the PMF self-check.
