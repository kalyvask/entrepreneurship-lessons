# PMF Measurement

You cannot manage what you do not measure. The trap is that PMF can be measured with metrics that look like signal but aren't. This file is the operational handbook for measuring PMF honestly.

## The Sean Ellis test

The most reliable single-number diagnostic.

**The question, asked of active users:**

> *"How would you feel if you could no longer use [product]?"*

**The options:**
- Very disappointed
- Somewhat disappointed
- Not disappointed (it isn't really that useful)
- N/A — I no longer use [product]

**Rule of thumb:** **40% or more** "Very disappointed" = PMF or close to it.

This is folkloric — there is no magic in 40 specifically — but the principle is robust. A high concentration of users who would feel acutely deprived = a desperate user base.

**Most pre-PMF startups land at 10–25%.** Climbing the curve from there means more *desperation* in the user base, not more users. Often the way to climb is to *narrow* the *who* — by removing customers who aren't desperate, the percentage in your remaining base goes up.

**Where to run it:**
- Active users only (not signed-up users, not trial users — *active*)
- Within your narrow *who* (not broadened)
- N >= 50 for meaningful signal (less than that, individual responses dominate)
- Mine the comment box of the "very disappointed" cohort — their reasons should map to the desperation markers ([`frameworks/rachleff_pmf.md`](rachleff_pmf.md))

**Common misuses:**
- Running on all users instead of active users
- Running on non-customers
- Running too small (N < 30)
- Reading only the number, not the comment box

## Retention curves

The other half of the PMF measurement story. Sean Ellis tells you *who feels desperate*; retention tells you *whether the desperation persists.*

**The setup:**
- Cohort by acquisition month (or week, for high-volume)
- Track: % of the cohort still active at week N
- Plot all cohorts on the same axes; X-axis is *weeks since acquisition*, Y-axis is *% still active*

**The three patterns:**

```
PMF retention (flattens above zero)
100% │\
     │ \
     │  \___
     │      \________________
     │                       
   0%├──────────────────────  weeks
     0          12          24

Pre-PMF retention (asymptotes to zero)
100% │\
     │ \
     │  \
     │   \____
     │        \____
     │             \______
   0%├──────────────────────  weeks
     0          12          24

Improving (curves bend up over time as cohorts get better)
100% │\
     │ \
     │  \         oldest cohort  ──────
     │   \___    next cohort     ════════
     │       \_  newer cohort    ━━━━━━━━━
   0%├──────────────────────  weeks
     0          12          24
```

**The diagnostic:**
- **Flat above zero** = PMF or strong product-need fit. The plateau is sticky users who will keep coming back.
- **Asymptotes to zero** = no PMF. Every customer eventually churns. *No matter what your other metrics show*, you do not have PMF.
- **Improving cohort-over-cohort** = approaching PMF. Newer cohorts retain better, meaning the product is improving for your *who*. Worth investing in. Keep going.

**Rules of thumb (rough):**
- SaaS: 30%+ active at 12 weeks for a paying cohort is good.
- Consumer: 25%+ DAU/MAU at 4 weeks is healthy.
- Marketplace: GMV per cohort holding flat or rising at 12 weeks.

These are *thresholds*, not targets. Real signal is the *shape* of the curve, not the level.

## Organic acquisition

The third pillar. Sean Ellis tells you who feels desperate; retention tells you it persists; organic acquisition tells you that desperation spreads.

**The metric:**

```
Organic % = (New customers from organic channels) / (Total new customers)
```

Where "organic" means: referrals, direct, search (non-paid), word-of-mouth, organic social, press, partnerships you didn't pay for.

**The signal:**
- **% climbing over time** — PMF approaching. The product is getting word-of-mouth.
- **% flat or declining** — concerning. You're growing the customer base but not creating advocates.
- **% > 40% during sustained growth** — strong PMF signal.

**The kill signal:**
- Revenue growth is high but organic % is declining. You're scaling paid acquisition; the bucket may have a hole. Stop pouring fuel until you fix it.

Rachleff: *"Paid growth is irrelevant; anyone with a credit card can buy attention. The only sustainable growth signal is organic word of mouth, and word of mouth requires desperation."*

## Composite signals

No single metric tells the truth. PMF is a *condition*, not a number. The honest assessment combines several signals:

| Signal | Weight | What "good" looks like |
|---|---|---|
| Sean Ellis "very disappointed" % | High | 40%+ |
| Retention curve shape (paying cohort) | High | Flattens above 30%-ish for SaaS by week 12 |
| Organic acquisition % | High | 40%+ of new customers from organic sources |
| Customer referrals (unsolicited) | Medium | Multiple per quarter without asking |
| Sales cycle length | Medium | Shrinking compared to early days |
| Cohort improvement | Medium | Newer cohorts retain better than older |
| Pricing power | Medium | You can raise prices without losing customers |
| NPS with detailed comments | Medium | NPS > 50, with comments that describe desperation markers |
| Logo / signup growth | Low | Vanity — necessary but not sufficient |
| Revenue growth | Low | Vanity if paid — useful if organic |

**The rule:** if you don't have *both* the Sean Ellis bar and a flat retention curve, you don't have PMF. Other signals matter, but those two are load-bearing.

## What does NOT count as PMF

❌ Revenue growth (alone) — can be paid-acquired with leaky retention
❌ Signups / waitlists — interest is not behavior
❌ Trial conversions — useful operationally; not PMF
❌ Investor enthusiasm — pre-PMF, this is narrative-driven
❌ "We're in 50 countries" — geographic spread is not depth
❌ Customer logos — vanity unless they're using and retaining
❌ Hiring growth — adds capacity, doesn't validate market
❌ Press coverage / awards — lagging, narrative

## When you don't have PMF — the diagnostic tree

```
Is Sean Ellis < 30% in your narrow who?
├── YES: the customers you have are not desperate enough
│   ├── Look at the over-performing slice
│   │   ├── Is there a subset converting 2x+? → Narrow further; serve them better. (Stage 06 — savor the surprise)
│   │   └── Is there no over-performing slice? → Pivot the who (Stage 07)
│   └── Or: rethink the value hypothesis (Stage 04)
│
└── NO (Sean Ellis is healthy in your narrow who):
    │
    ├── Is the retention curve asymptoting to zero?
    │   └── YES: customers love it on first try, then churn
    │       ├── Likely engagement issue → strengthen the value over time
    │       ├── Or the who is mostly tourist (false-positive) → re-narrow
    │       └── Or the product solves the job once but no ongoing demand → reconsider business model
    │
    ├── Is organic acquisition stagnant?
    │   └── YES: customers retain but don't refer
    │       ├── Likely happy-but-not-evangelist → why? probe with interviews
    │       ├── Distribution may be the issue (not who) → pivot the how
    │       └── The pain may be embarrassing (e.g., financial trouble) → expect lower viral
    │
    └── All three are healthy but you don't *feel* PMF?
        └── You may have it. Reread the section "Hard signals" in stages/06.
```

## Reporting PMF status

To yourself, your team, and your investors. Honest format:

```
PMF STATUS — [Date]

In our narrow who segment ([segment name]):

1. Sean Ellis "very disappointed" %:    [number] (N=[active users in segment surveyed])
2. Retention curve, paying cohort:       Plateaus at [number]% at week 12 / asymptotes to zero
3. Organic % new customers (last 30d):   [number]%
4. Cohort trend:                         Improving / flat / declining
5. Pricing test (raised X% on new):      [outcome]

Verdict: [PMF / approaching PMF / not yet / need to pivot]

Most important next action: [specific, time-boxed]
```

If you cannot fill this in cleanly, you do not yet have PMF *or* the data to claim it.

## Where this lives in the journey

- [Stage 06 — PMF Measurement](../stages/06_pmf_measurement.md) — when you run this
- [Stage 07 — Pivot or Persevere](../stages/07_pivot_or_persevere.md) — what to do if you don't have it
- [`playbooks/pmf_assessment.md`](../playbooks/pmf_assessment.md) — the operational checklist
- [`templates/pmf_survey.md`](../templates/pmf_survey.md) — Sean Ellis survey template

## Source

The Sean Ellis test is from Sean Ellis, growth advisor at Dropbox, Eventbrite, LogMeIn. Retention curve discipline is standard in startup analytics; Brian Balfour and Lenny Rachitsky's writing has popularized the cohort-curve diagnostic. The Rachleff framing of organic-only signal is from STRAMGT 514. See [`frameworks/rachleff_pmf.md`](rachleff_pmf.md).
