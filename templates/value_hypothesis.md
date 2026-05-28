# Value Hypothesis — Template

Fill this out. One page. Specific enough to build to. Update only when you've earned a change through evidence.

---

## Project / Venture: ___________________________

## Date: ___________________________

## Version: ___________________________

---

## INSIGHT (the foundation)

The non-consensus belief about how the world is changing that the value hypothesis rests on:

> Because of [inflection / change happening in the world], it is now possible/necessary to [new capability], which existing players cannot pursue because [structural reason — RPV, incentives, channels, etc.].

Filled in:

> Because of __________________________________________________________
> __________________________________________________________________
> __________________________________________________________________
>
> it is now possible/necessary to ____________________________________
> __________________________________________________________________
>
> which existing players cannot pursue because _______________________
> __________________________________________________________________
> __________________________________________________________________.

---

## THE VALUE HYPOTHESIS

### What

The product. One sentence. Specific enough that an engineer could begin designing to it.

> ___________________________________________________________________
> ___________________________________________________________________
> ___________________________________________________________________

### Who

The customer. Narrow enough to identify 50 specific people today. Defined by **behavior and circumstance**, not just demographics.

> ___________________________________________________________________
> ___________________________________________________________________
> ___________________________________________________________________
> ___________________________________________________________________

**Specificity check:** can I name 10 real people who fit this? List them in a working doc.

### How

Delivery, distribution, monetization.

- **Delivery:** ____________________________________________________
- **Distribution:** ________________________________________________
- **Pricing model:** _______________________________________________
- **Estimated price point:** _______________________________________

---

## LEAP OF FAITH

The **one** thing that must be true for this hypothesis to work. Behavioral, not technical. One sentence.

> ___________________________________________________________________
> ___________________________________________________________________
> ___________________________________________________________________

**Discipline check:**
- [ ] One sentence
- [ ] Describes a behavior, not a technical capability
- [ ] If false, the business has no path
- [ ] I can design an experiment to test it directly

---

## WHAT'S NOT IN V1

Explicit list of things I'd want to build but won't in v1:

- ___________________________________________________________________
- ___________________________________________________________________
- ___________________________________________________________________
- ___________________________________________________________________
- ___________________________________________________________________
- ___________________________________________________________________

**The discipline:** every feature past what tests the leap of faith is wasted work.

---

## BACK-OF-ENVELOPE UNIT ECONOMICS

Rough numbers — sanity check, not financial planning:

- **Pricing (ARPU per month):** $______
- **Gross margin estimated at scale:** ______%
- **Acquisition cost estimated at scale:** $______
- **Churn estimated at scale (monthly):** ______%

Computed:
- LTV = $______
- LTV / CAC = ______
- Payback (months) = ______

**Pass / Fail check:** LTV/CAC > 3? Payback < 24mo? If no — restructure pricing, channel, or who.

See [`frameworks/unit_economics.md`](../frameworks/unit_economics.md) for math.

---

## TEST DESIGN

How I'll test this:

- **Phase 1 (concept test):** What will I run? What's the success threshold?
- **Phase 2 (implementation test, if needed):** What will I sprint on?
- **Phase 3 (MVP test):** What's the build, and what's the success threshold?

See [`playbooks/validation_sequence.md`](../playbooks/validation_sequence.md).

---

## FOUNDERS' FEEDBACK MEETING

Before committing to build:

- [ ] Reviewed with co-founder(s)
- [ ] Reviewed with at least 1 advisor / mentor
- [ ] Reviewed with at least 1 customer (in the new *who*)
- [ ] Reviewed with at least 1 skeptic who pushed back

Key pushbacks received:

1. ___________________________________________________________________
2. ___________________________________________________________________
3. ___________________________________________________________________

How I'm addressing them: __________________________________________

---

## DECISION

- [ ] Proceed to Stage 05 (MVP build)
- [ ] Refine hypothesis — return to Stage 02 (more discovery)
- [ ] Refine hypothesis — return to Stage 01 (different insight)
- [ ] Park this candidate; pursue alternate

Decision notes:

___________________________________________________________________
___________________________________________________________________
___________________________________________________________________

---

## VERSION HISTORY

| Version | Date | What changed | Why |
|---|---|---|---|
| v1 | | | |
| v2 | | | |

---

**Discipline:** changes to the value hypothesis should be driven by *evidence*, not by *new ideas*. Track what evidence triggered each version.

See [`stages/04_value_hypothesis.md`](../stages/04_value_hypothesis.md) for the discussion.
See [`frameworks/pmf.md`](../frameworks/pmf.md) for the framework.
