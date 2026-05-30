# Stage 07 — Pivot or Persevere

> Rachleff's rule: iterate the *who*, sometimes the *how*, never the *what* — adding features does not make anyone desperate.

The pivot decision is the most important strategic decision a pre-PMF company makes. It is also the most commonly mishandled.

Most teams pivot too late, too small, or in the wrong direction. They keep building features. They keep convincing themselves the current customers "just need a little more time." They run out of money pursuing a fantasy customer who is never going to be desperate enough.

The discipline of this stage is to take the data honestly and make a clean call: pivot the *who*, pivot the *how*, persevere, or — rarely — restart.

## When you are in this stage

- You have 3–6 months of MVP/early product evidence.
- Your PMF self-check (Stage 06) is showing red on most dimensions.
- Customers exist but they aren't desperate enough — they use the product, they like it, but they don't refer, they churn, they hedge on pricing.
- Or: the metrics are *fine* but you feel like you're pushing the boulder uphill — every win is a hard-fought sale, every renewal a negotiation.

If your metrics are climbing organically, you don't have a pivot decision. You have a perseverance decision: keep going.

## The taxonomy

The course's framing reduces pivots to three categories. The vocabulary is precise — using it precisely will save you months of confusion.

### Pivot the *who* — almost always the right move

You hold the *what* (your product, your insight) and change *who* you're selling it to.

**Example: Broadcom.** The insight was that shrinking semiconductor geometries made it economical to implement analog functions in digital silicon. First *who*: cable set-top box transceivers. The cable industry didn't move fast enough. Pivot the *who*: Ethernet LAN providers, who were starved for cheap, fast, integrated chips. The pivot was the company.

**Example: Wealthfront.** Started broadly as "automated investing." Pivoted progressively narrower: not all retail investors, but engineers in tech. Not all engineers, but those at consumer-tech companies. Not all of those, but pre-IPO engineers with under $1M in assets. Same *what* (automated investing). The narrowing-as-pivot is the same move repeated.

**Why pivot the who is usually right:**
- The insight is intact — your reason for building the product is still defensible.
- The product is mostly intact — the engineering work isn't wasted.
- The *who* is the variable most likely to be wrong on first attempt — most teams over-broaden, and the narrow-down is where PMF lives.

**When to do it:**
- You have product-market mismatch, not product-quality issues.
- Some segments of customers retain and refer, others don't. Find the seam.
- A particular customer is using the product 5× more than the others — that's a *who* signal, not noise.

### Pivot the *how* — sometimes right

You hold the *what* and *who* and change how you reach them, deliver, or monetize.

**Example sources of how-pivots:**
- Inside sales → channel
- Direct → marketplace
- Per-seat → usage-based pricing
- Self-serve → sales-led (or vice versa)
- Subscription → freemium → trial
- Enterprise → mid-market sales motion

**Why this can be right:** sometimes the value hypothesis is sound and the *who* is correct, but the friction of how you reach them or the way you price is what's broken. A $50K annual contract for a tool a customer would happily pay $500/mo for is a *how* problem, not a *what* problem.

**When to do it:**
- Customers love the product but the sales cycle is too long.
- Conversion rates are fine but acquisition cost is too high.
- Retention is great but expansion is poor (pricing model issue).
- Pilot-to-paid is leaking (sales motion mismatch).

### Persevere — when you have signal, push harder

Sometimes the right answer is to keep going. Specifically when:

- The retention curve is improving cohort over cohort, even if absolute numbers are low.
- A subset (the over-performing slice) is showing PMF behaviors even if the broader base isn't.
- The Sean Ellis test is climbing — 18% → 26% → 35% over three quarters.
- Customers in your narrow *who* are converting; you just don't have enough of them yet.

The mistake to avoid: declaring perseverance because you're emotionally invested. Test the data, not the wish.

### Restart — the *what* changes

Changing the *what* is what Rachleff calls a **restart**, not a pivot. Restarts are rare and rarely successful.

The seductive example everyone raises: **Instagram.** Started as Burbn (a location check-in app). Pivoted to photo sharing. Looks like a *what* change.

Rachleff's correction: he treats Instagram as a restart, not a pivot. The original product had nothing to do with photos; what actually succeeded was the mobile photo upload to Facebook, which makes it a complete restart. The share of restarts that succeed is exceptionally low, and he avoids using such examples because outliers distort the probabilities.

The point: don't model your decision on the rare exceptions.

**Why restarts are usually wrong:**
- Changing the *what* obsoletes the original insight. You're now competing on execution in a market other people are already in.
- The engineering work is wasted.
- The team's domain knowledge is partially wasted.
- You've used up time/money/morale on the previous bet.
- Most importantly: if the original *what* was actually grounded in an insight, the *who* almost certainly has a desperate customer somewhere. Finding them is cheaper than restarting.

**When a restart is genuinely right:**
- The original insight was wrong (not just the *who*). The fundamental belief about how the world is changing turned out to be false.
- You discovered, through customer development, an *adjacent* insight that's stronger than the original. New insight, new bet.
- The pace of change in the space made the original insight obsolete (rare).

Even then: ask yourself if a new founding team would attack this insight from scratch. If yes, you may have a different company on your hands.

## The decision framework

A structured way to think through the call. Run this as an exercise — not as a pitch to investors. As an honest reckoning with yourself and your co-founders.

### Step 1 — Diagnose the failure mode

Look at the PMF self-check from Stage 06. Where specifically is it red?

- **Red on the *who*:** Customers exist, behave, but they're the wrong customers. *Symptom:* enthusiastic users who don't pay, or paying users who don't retain, or some segments converting wildly better than others. → **Pivot the who.**

- **Red on the *how*:** Customers exist, want it, but the sales/pricing/distribution motion is fighting you. *Symptom:* sales cycles too long, conversion rate low, acquisition cost high, expansion poor. → **Pivot the how.**

- **Red on usage/retention even in the right *who*:** Customers in the narrow *who* aren't desperate enough. *Symptom:* great pitch, lukewarm usage. → **Re-examine the insight.** Possibly back to Stage 02.

- **Red on the insight itself:** What you believed about the world isn't true. *Symptom:* no segment shows desperation; the entire space behaves indifferently to your product. → **Restart, or shut down.**

### Step 2 — Identify the over-performing slice

Scott Cook's "savor the surprise." Look in the data:

- Which customer cohort has 2–5× retention vs the average?
- Which customer used the product the most? What's true about them that's NOT true about the average?
- Which acquisition channel is converting and retaining? What's true about the buyer mindset there?
- Which feature was used at 10× the rate of others?

The over-performing slice tells you where PMF is, if there is PMF anywhere in your data. Pivot toward it.

### Step 3 — Articulate the new value hypothesis

If you're pivoting, write the new value hypothesis using the [Stage 04](04_value_hypothesis.md) template. *What / who / how / leap of faith.*

If you're persevering, restate the original value hypothesis. Has anything changed in your understanding? Update the leap of faith to reflect the data.

If you're restarting, you're effectively going back to Stage 01.

### Step 4 — Decide the test

Pivots are also experiments. The new value hypothesis needs to be tested. Set up:

- **Timeframe:** How long will you give the new hypothesis? (Be specific — 3 months, 6 months.)
- **Threshold:** What evidence will count as "the pivot worked"? (Concrete: 5 customers in the new *who*, retention curve flatening, organic % rising.)
- **Trigger for next decision:** If by [time], the [threshold] hasn't moved — what's the next move? (Pre-commit so you don't slip back into wish-thinking.)

### Step 5 — Communicate honestly

The pivot has communication consequences:

- **Existing customers:** Will the pivot leave them stranded? How much do you owe them? (If you'd recently sold to a customer in the old *who* and the pivot makes you abandon them — be honest with them.)
- **Investors:** Pivots are normal but they need a story that holds together. The story should be the data, not the narrative.
- **The team:** Some people joined for the old vision. Some won't make the new one. Acknowledge it.
- **Co-founders:** Pivots are also relationship tests. Do this in writing, not just verbally.

## Common pitfalls in this stage

| Failure | What it looks like | Why it kills you |
|---|---|---|
| Adding features to lukewarm customers | "If we just add X, they'll convert" | Rachleff calls this lunacy. Features don't make people desperate. |
| Restart instead of pivot | "This product isn't working, let's build something else" | You waste the insight. The *who* was almost certainly the issue. |
| Death pivot | Pivoting in circles every 2 months | You don't give any single hypothesis time to play out. |
| Pivoting too late | "We'll give it one more quarter" — repeated 4 times | Runway evaporates; emotional sunk cost mounts. |
| Pretending to pivot | Changing the language but not the product | New deck, same hypothesis. |
| Pivoting only the deck | Internal narrative changes, behavior doesn't | The investors see a pivot, the customers see nothing. |
| Pivoting because of one disappointed customer | "Big-name lost the pilot, let's restart" | Your data is small; don't over-weight outliers. |
| Pivoting because of investor pressure | "Our VC thinks we should pivot to AI agents" | Your VC is not the customer. Test, don't follow. |

## A note on "perseverance"

There's a counter-pressure in this section: most founders pivot too late. But some pivot too early.

The signal that perseverance is right:
- The retention curve is **improving** cohort over cohort, even if absolute is low.
- A specific narrow *who* is **converting** at high rates, even if there aren't enough of them yet.
- Customers in that narrow segment **refer** organically, even if you can't yet measure organic acquisition % as meaningful.

These are signals that PMF is approaching but not yet hit. The right move is to **enhance the good** — find more of the converting customers, deepen the product for the high-retention cohort. Not pivot.

## Exit criteria

You exit this stage in one of three states:

**State 1: Pivoted to a new value hypothesis** → back to [Stage 04](04_value_hypothesis.md), then through [Stage 05](05_mvp_build.md) and [Stage 06](06_pmf_measurement.md) again with the new hypothesis.

**State 2: Perseverance, with sharper focus** → enhance the good, find more of the over-performing slice, refine your *who*. Stay in [Stage 06](06_pmf_measurement.md) measurement loop.

**State 3: Achieved PMF** → execution phase. The methodology of pre-PMF (build to learn) gives way to the methodology of post-PMF (build to execute). New skills, new tempo, new playbook. Some pointers: [`frameworks/crossing_the_chasm.md`](../frameworks/crossing_the_chasm.md) on bowling pins and the chasm, [`frameworks/disruption_theory.md`](../frameworks/disruption_theory.md) on watching for incumbent moves.

If you reach the point where you've pivoted twice without finding the desperate customer, and your data doesn't show an over-performing slice — the honest move is to shut down or restart. Don't go to a third pivot of the same value hypothesis.

## Required reading

- [`frameworks/pmf.md`](../frameworks/pmf.md) — iterating the *who*, not the *what*
- [`frameworks/lean_startup.md`](../frameworks/lean_startup.md) — Ries's pivot taxonomy
- [`frameworks/disruption_theory.md`](../frameworks/disruption_theory.md) — RPV; why incumbents fail
- [`playbooks/pivot_decision.md`](../playbooks/pivot_decision.md) — running a pivot decision in practice
- [`templates/pivot_memo.md`](../templates/pivot_memo.md) — the pivot memo

## Agent partner

- `/ent-pivot-coach` — runs a structured pivot diagnosis based on your data. Tells you whether you have a *who*, *how*, or *what* problem; finds the over-performing slice you're averaging out ("savor the surprise"); pushes back on emotion-driven decisions.
- `/ent-red-team` — pressure-tests the new value hypothesis before you commit
