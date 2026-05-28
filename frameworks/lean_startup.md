# The Lean Startup (Eric Ries)

> *"The scientific method has been the agreed-upon approach to achieving discovery for more than 400 years. Yet it was not applied to startups until Steve Blank started writing teaching notes that became Four Steps to the Epiphany. Eric Ries, Blank's student, then wrote The Lean Startup — same content, more accessible. Blank's is the Old Testament. Ries's is the New Testament."* — Andy Rachleff

Eric Ries was Steve Blank's student. His book *The Lean Startup* (2011) is the accessible packaging of customer development. The vocabulary it introduced — *build-measure-learn*, *validated learning*, *MVP*, *pivot vs. persevere*, *innovation accounting*, *vanity metrics* — is now standard in entrepreneurship. This file is the compressed reference.

## The core claim

A startup is **a human institution designed to create a new product or service under conditions of extreme uncertainty.**

The unsexy implication: a startup is *not* a small big-company. It is a different kind of organization, operating in different terrain, requiring different skills. The methods of stable execution (Gantt charts, MBO, KPIs) corrupt rather than help. Different uncertainty → different method.

The method is **scientific.** Hypothesize, test, learn. The variable being optimized is *the rate at which you learn.*

## Build-Measure-Learn

The Lean Startup feedback loop:

```
    ┌──────────────┐
    │   IDEAS      │
    │ (hypotheses) │
    └──────┬───────┘
           │
           ▼
       (Build)
           │
           ▼
    ┌──────────────┐
    │   PRODUCT    │
    │  (experiment)│
    └──────┬───────┘
           │
           ▼
      (Measure)
           │
           ▼
    ┌──────────────┐
    │     DATA     │
    │  (behavior)  │
    └──────┬───────┘
           │
           ▼
       (Learn)
           │
           ▼
      [Pivot or Persevere]
```

Four moves:

1. **Hypothesize** — articulate the leap-of-faith assumption (see below).
2. **Build** the smallest experiment that tests it.
3. **Measure** behavior, not intent.
4. **Learn** — pivot or persevere.

Iterate faster than competitors can. *The variable Ries cares about most: the rate at which you learn.*

## Validated learning

A successful experiment is **not one that proves your hypothesis.** It is **one from which you learn.** Outcome is not the test of decision quality — process is.

This is hard to internalize because it conflicts with intuition. You'll feel like a failed experiment is a setback. The framing is: a *fast* failed experiment is a victory. It generated information cheaply. A *slow* failure (six months building the wrong thing) is a real setback because the learning came expensively.

## Leap of faith assumptions

The hypotheses your business depends on. Specifically the ones you have no evidence for. Ries categorizes them:

- **Value hypothesis** — does the product create the value we think it does for the customer?
- **Growth hypothesis** — will new customers find the product through the mechanism we think they will?

(Rachleff's framing differs slightly: the value hypothesis is the *what/who/how* itself, and the *leap of faith* is the one assumption underneath it. Both vocabularies are useful; hold them parallel.)

## Minimum Viable Product (MVP)

The Ries MVP: **the smallest possible product capable of testing the leap of faith.**

The point is *learning*, not *minimum scope to launch.* An MVP might be:

- **A video** explaining the product (Dropbox's MVP — they had no product when they tested demand).
- **A concierge service** where you manually do the work behind the scenes (Food on the Table started this way).
- **A landing page** with a price and a buy button that emails the founder when clicked.
- **A wizard-of-Oz product** where what looks like AI is a human responding to prompts.
- **A small, broken first version** that does one thing well enough to test the value.

The discipline: every feature past what's required to test the leap of faith is *wasted work.* The goal of v1 is data, not delight.

(Rachleff/Vrionis vocabulary refinement: video, landing page, and Figma prototypes are not "MVPs" in their definition — they are *concept tests* and *implementation tests* in a three-phase sequence. An MVP in their framing is **usable, paid, and learning-focused.** Use whichever vocabulary your team adopts, but pick one and be consistent.)

## The five whys

A root-cause analysis technique Ries borrowed from Toyota's manufacturing system, adapted for startup operations.

When something goes wrong (an outage, a deployment failure, a customer churn, a missed goal):

1. Why did the thing go wrong?
2. Why did *that* cause it?
3. Why did *that* condition exist?
4. Why was that allowed?
5. Why is the systemic root cause?

The pattern: technical problems usually have human/process root causes 3–5 questions deep. The action item is at the deepest "why," not the surface symptom.

Rachleff models the five whys in customer conversations too: drill past polite answers until you find the root objection. *"I do five whys to you all the time in this class. Have you noticed?"*

## The pivot taxonomy

Ries enumerates ten pivot types. The most useful ones for the journey:

- **Zoom-in pivot** — a single feature becomes the whole product.
- **Zoom-out pivot** — the whole product becomes one feature of a larger one.
- **Customer segment pivot** — same product, different audience (Rachleff's *pivot the who*).
- **Customer need pivot** — different problem in same audience.
- **Platform pivot** — application becomes platform, or vice versa.
- **Business architecture pivot** — high-margin/low-volume to low-margin/high-volume, or vice versa.
- **Value capture pivot** — different monetization model (Rachleff's *pivot the how*).
- **Engine of growth pivot** — different growth engine.
- **Channel pivot** — different distribution.
- **Technology pivot** — different way to deliver same value.

Rachleff compresses this into three options: change the *who* (pivot), the *how* (pivot), or the *what* (restart, rarely succeeds). The Ries taxonomy is more granular; Rachleff's is sharper for decision-making.

See [Stage 07 — Pivot or Persevere](../stages/07_pivot_or_persevere.md).

## Innovation accounting

Tying leap-of-faith assumptions to quantitative milestones so the team can tell if it is progressing or just busy. Three steps:

1. **Establish the baseline.** What is the current state of the metric that matters?
2. **Tune the engine.** Run experiments to improve toward the leap of faith.
3. **Pivot or persevere.** At the gate, decide.

Rachleff endorses the idea in spirit but warns against vanity metrics: *"Revenue is signal, not source. Necessary but not sufficient. We don't need additional metrics. We need one good one and we track that obsessively."*

## Vanity vs. actionable metrics

- **Vanity metrics** — total users, total signups, total revenue. Look impressive. Don't tell you whether the hypothesis is true.
- **Actionable metrics** — cohort retention, per-customer revenue, organic referral rate. Show whether changes you make actually move the needle.

Vanity metrics seduce because they look like progress. Actionable metrics tell you what's actually happening.

A vanity metric example: *"We added 10,000 users this month!"* Cohort metric: *"Of the 10,000 users we added, 2,000 came back week 2; 800 came back week 4; 200 are still active at week 12. The retention curve asymptotes toward zero."* The vanity metric makes you feel good. The cohort metric tells you you don't have PMF.

## The three engines of growth

Ries identifies three growth mechanisms. Most companies are dominated by one — multi-engine companies are rare and usually less clear in narrative.

- **Sticky engine** — high retention, low churn. Growth = new customer rate − churn rate. Wealthfront. Salesforce.
- **Viral engine** — each customer recruits more than one new customer (viral coefficient > 1). Self-amplifying. Dropbox referrals. Facebook.
- **Paid engine** — predictable LTV/CAC > 3 lets you spend paid acquisition profitably. Etsy. Most subscription DTC.

Diagnosis: which engine is your company actually using? Most pre-PMF teams *think* they have a viral engine because of a single referral spike; *actually* they have a paid engine that hasn't been profitably tuned. Knowing which engine is yours sharpens what to measure and what to invest in.

## Cohort analysis

The fundamental tool of innovation accounting. Group customers by acquisition month (or week). Plot the metric you care about (retention, revenue per customer, organic referral rate) over time *for each cohort.*

Patterns to look for:

- **Improving cohorts** — each new cohort does better than the last. Strong signal: the product is getting better and PMF is approaching.
- **Flat cohorts** — same outcome regardless of when they signed up. Stable but not improving. PMF unclear.
- **Declining cohorts** — newer cohorts retain less than older ones. Bad signal: usually means you're broadening *who* and losing PMF.

## The connection to Rachleff

The frameworks overlap heavily. Differences in emphasis:

- **Ries:** general method, broad applicability (corporate innovation, consumer, B2B, etc.). More tolerant of MVPs as concept tests.
- **Rachleff:** focused on tech (IP-driven) businesses, big outcomes. Sharper on the *desperation* threshold; less tolerant of "needy" customers. Three-phase validation more rigorous than Ries's MVP-only loop.

Both agree on:
- Learning rate is the primary variable.
- Validated learning > validated assumptions.
- Pivots are normal; restarts are dangerous.
- Vanity metrics kill teams.
- A startup is a fundamentally different organization from a stable execution business.

Both disagree (subtly) on:
- The role of explicit growth-hypothesis testing pre-PMF (Rachleff is stricter: don't test growth until value is validated).
- What counts as an MVP (Rachleff: usable, paid; Ries: anything that tests the leap of faith).

In practice, hold both: Ries's vocabulary for the loop, Rachleff's discipline for the threshold of what counts as PMF.

## Where this lives in the journey

- [Stage 04 — Value Hypothesis](../stages/04_value_hypothesis.md) — articulating leap of faith
- [Stage 05 — MVP Build](../stages/05_mvp_build.md) — the build-measure-learn loop in practice
- [Stage 06 — PMF Measurement](../stages/06_pmf_measurement.md) — cohort analysis, innovation accounting
- [Stage 07 — Pivot or Persevere](../stages/07_pivot_or_persevere.md) — the pivot taxonomy

## Source

*The Lean Startup* — Eric Ries (Crown, 2011). The book runs ~330 pages. The first 7 chapters are the load-bearing ones; chapters 1–6 cover the foundations (build-measure-learn, MVP, leap of faith); chapter 7 introduces the value hypothesis vocabulary. The course assigns those chapters specifically.
