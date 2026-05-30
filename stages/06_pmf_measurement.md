# Stage 06 — Product-Market Fit Measurement

> Rachleff's framing: in plain terms, product-market fit means you've found a market that is desperate for your product. The technical version is a validated value hypothesis, and you can't validate one without organic growth. Paid growth doesn't count — anyone with a credit card can buy attention. The only durable growth signal is organic word of mouth, and word of mouth only happens when customers are desperate.

The most common mistake teams make at this stage is **claiming PMF before they have it.** Every metric becomes wishfully interpreted: a spike in signups becomes "traction"; a single enterprise pilot becomes "market validation"; a 30% MoM revenue growth becomes "PMF."

PMF is a specific, falsifiable, measurable condition. This file describes how to measure it honestly.

## When you are in this stage

- You've shipped an MVP from [Stage 05](05_mvp_build.md).
- You have at least 5 paying customers in your narrow *who* segment.
- You have 2–6 months of usage and behavioral data to work with.
- You are not sure whether you have PMF. (If you're sure, you don't — see below.)

## What PMF actually is

A useful set of definitions, in increasing precision:

**The casual definition.** Dogs are eating the dog food. The market wants the product.

**The intermediate definition.** Customers refer other customers without being asked. They mention the product unprompted. They are angry when it's down. They behave like advocates inside their organizations.

**The technical definition (Rachleff).** A validated value hypothesis with organic growth. The product solves a desperate problem for a specific *who*, the customer behavior matches the hypothesized model, and the customer base grows through word-of-mouth without paid acquisition.

**The economic definition.** LTV/CAC > 3 at scale, organic acquisition meaningful (>40% of new customers), retention curve flattens (not asymptotes to zero), payback < 12 months, gross margin healthy.

You need to be at all four definitions to claim PMF.

## The signals — in order from soft to hard

### Soft signals (necessary, not sufficient)

These tell you you *might* be approaching PMF. None alone confirms it.

**Customer enthusiasm.** Customers say things like "this changed how we operate" without being prompted. They appear in your Slack channel asking questions, asking for features, asking when you'll release X.

**Sales cycle shrinking.** The first 5 customers took months each. Customers 6–15 close in days. The pitch is *easier*; in fact, *they're selling themselves.*

**Unsolicited referrals.** You get inbound. Strangers email you. People show up to your launch event you don't know.

**Use frequency.** Active users use the product more often than your usage hypothesis predicted, and the curve isn't decaying.

### Medium signals

These move from "might have PMF" to "probably have PMF."

**The Sean Ellis test.** Survey active users with the question: *"How would you feel if you could no longer use [product]?"* with options:
- Very disappointed
- Somewhat disappointed
- Not disappointed (it isn't really that useful)
- N/A — I no longer use [product]

**Rule of thumb:** If **40% or more** of active users say "Very disappointed," you have PMF or are close. This is a high bar — most pre-PMF startups land at 10–25%. The exact 40% is folkloric; the principle is robust: a high concentration of users who would feel acutely deprived = a desperate user base.

**Retention curve flattens.** Plot weekly/monthly retention by cohort. PMF looks like a **curve that bends and then stays flat (or rises)** above zero. Pre-PMF looks like a curve that asymptotes to zero — *every cohort eventually churns out.* If retention asymptotes to zero, you do not have PMF, no matter what other metrics show.

For SaaS: weekly logged-in usage holding above 30% at 12 weeks for a non-trivial cohort is a strong signal.
For consumer: daily/weekly active above 25% at 4 weeks for a meaningful cohort.

**Organic acquisition % rising.** Trend the share of new customers that come through organic / WOM channels — referrals, search, direct, organic social. As a share of new acquisitions, this should be *climbing* during PMF approach, not flat or declining.

**NPS above 50 with detailed reasons.** NPS as a number is noisy. NPS with the comment box mined is signal. If promoters describe *the specific desperation marker* — "I would have to go back to spending 15 hours/week on this" — that's behavioral evidence.

### Hard signals (you're at PMF)

**Customers volunteer to sell your product for you.** John Vrionis's reformulation. Customers proactively bring you into other accounts. They speak at your events. They demo to their peers without being asked.

**You're running, not pushing.** Customer success teams are putting out fires. Sales teams are saying "we can't keep up with inbound." Engineering is rate-limited by capacity, not by what to build. The org has shifted from "find PMF" to "scale PMF."

**Pricing power.** You raise prices and most customers don't blink. Or you can raise prices on new customers without losing them.

**Investors come to you.** This is a *lagging* signal — but a real one. Investor interest in companies pre-PMF is a function of narrative; post-PMF it's a function of math. When the math is what's attracting them, you have PMF.

## What does NOT count as PMF

A list, because every team gets seduced by at least one of these:

❌ **Revenue growth.** Anyone with a credit card can buy attention. If your customers are mostly paid-acquired and churning at the back, revenue masks the truth. Look at *net new MRR from organic* — much smaller number, much truer signal.

❌ **Signups.** A vanity metric. Signups without behavior are noise.

❌ **Trial conversions.** Useful operationally, but a 5% trial→paid rate with no retention is worse than a 1% rate with 90% retention.

❌ **Press coverage / awards.** Lagging, narrative-driven. Means nothing about the market.

❌ **Investor enthusiasm pre-PMF.** Investors at the seed and Series A stage are buying narrative. By Series B, they're buying math.

❌ **Hiring growth / fundraising amount.** Pour fuel on an unproven fire and you scale waste.

❌ **"We're in 50 countries."** Geographic spread is not depth. Depth in one segment > breadth across many.

❌ **"Our customer logos."** Logos are vanity. Active, paying, retained, referring customers in your *who* are the signal.

## The diagnostic: a structured PMF self-check

Run this every quarter pre-PMF. Be brutal.

```
PMF SELF-CHECK
1. The who:
   - Have we held the who narrow, or have we broadened to accommodate the customers we got?
   - If we got non-who customers, are we counting them as PMF signal? (We shouldn't.)
   - Of customers in our narrow who: how many are paying, retained at 12 weeks, and using weekly?

2. The leap of faith:
   - Is the behavioral assumption verified? Genuinely yes/no/ambiguous?
   - If verified — by what specific behavior, not by general enthusiasm?
   - If still ambiguous after MVP — why? Was the MVP not diagnostic enough?

3. Retention:
   - Plot the weekly retention curve by cohort. Where does it stabilize? At zero, or above?
   - Is the curve improving cohort over cohort?
   - For paying customers (not free): same questions.

4. Organic acquisition:
   - Trend organic % of new customers over last 6 months.
   - Is it climbing, flat, or declining?
   - Could we stop paid acquisition tomorrow and still grow? (At PMF, the answer is usually yes.)

5. Sean Ellis test:
   - Run it on active users in the narrow who.
   - What % say "very disappointed"?
   - Read the comment box for the "very disappointed" cohort. Do their reasons map to the desperation markers?

6. The "tell" tests:
   - Do customers refer without being asked?
   - Do customers demand features in a way that says "I depend on this product"?
   - Are sales cycles shrinking? Has the friction of getting a new customer dropped?
   - Do you have inbound interest you didn't generate?
```

If you score positively on all 6, you have PMF.
If you score positively on 1–3, you don't, no matter the revenue.
If you score positively on 4–5, you might — and now you're trying to figure out the gap.

## "Fix the bad" vs "enhance the good"

A specific course principle worth flagging here. When you're in this stage and something's underperforming, you have two options:

**Option A: Fix the bad.** Take the cohort that didn't convert and try to convert them. Take the feature that wasn't used and improve it. Take the segment that didn't retain and target them more.

**Option B: Enhance the good.** Take the cohort that DID convert and find more like them. Take the feature that IS used and double down on it. Take the segment that DID retain and serve them more deeply.

**The course's principle: enhancing the good improves growth. Fixing the bad almost never does.**

The intuition: the customers you didn't get were not desperate. The customers you did get were. Investing in the desperate ones — making the product better for them, finding more of them — is how you accelerate. Trying to convert the indifferent ones is fighting their nature, and it almost always fails.

When you're 90% certain you have PMF: enhance the good.
When you're 50% certain: enhance the good for the slice where you definitely do.

## Scott Cook's "savor the surprise"

The course's recurring move. **The signal is in the surprise**, not the predicted. If a segment is converting at 3× the rate of the rest, that's not noise to be averaged out — that's the seam of where PMF lives.

The famous example: Airbnb. Listings with professional photos converted 3× higher than amateur photos. Instead of optimizing the rest, they sent photographers to high-potential listings — *they enhanced the good.* That single intervention may have been the most important PMF-bridging move the company made.

For your own search: read your data looking for **what is over-performing**, not what is on-trend. The cohort that retains at 80%. The customer who refers 10 others. The segment that uses 10× more than average. **That's where PMF lives. Find more of them.**

## Common failure modes in this stage

| Failure | What it looks like | Why it kills you |
|---|---|---|
| Declaring PMF too early | "We have 50 customers, we're at PMF" | You burn capital scaling something that isn't actually proven |
| Vanity metrics | Revenue without retention; signups without activation | The math at scale will reveal the lie |
| Broadened *who* | "We started selling to enterprise *and* SMB *and* developers" | Diluted signal; you can't tell what's working |
| Paid acquisition masking churn | High net new MRR via ads; retention asymptotes to zero | Paid fuel + leaky bucket = scaling waste |
| Fixing the bad | Pouring engineering into the segment that doesn't convert | The desperate customers are the ones you have, not the ones you don't |
| Surveying wrong people | Sean Ellis test on inactive users or non-customers | The number means nothing |
| Anecdote-driven | "This one VP said the product changed her life" | One advocate is not a market |
| Premature investment in growth | Hiring sales/marketing before PMF | Adds fuel to an unproven fire — Rachleff's "fire" metaphor |

## When you don't have PMF (the hard truth)

Most teams at this stage will discover they do not have PMF.

The right move is not to keep pushing. The right move is to **pivot** — change the *who*, sometimes the *how*. (See [Stage 07 — Pivot or Persevere](07_pivot_or_persevere.md).)

It is almost never to change the *what.* The insight that brought you here was real; the *who* may have been wrong, but the underlying belief about the inflection probably wasn't. (See [`frameworks/pmf.md`](../frameworks/pmf.md) on why iterating the *what* obsoletes your own insight.)

Holding the *what* and changing the *who* is what Rachleff calls a pivot. Restarts (changing the *what*) are different and almost always fatal.

The other right move is **to stay.** If your retention curve is improving cohort over cohort, if your Sean Ellis number is climbing, if your narrow *who* is converting at high rates but you don't yet have 50 of them — keep going. PMF is not a step function in most companies. It's a gradient.

## Exit criteria

You move to [Stage 07](07_pivot_or_persevere.md) (for a decision) or — if PMF is achieved — to the post-PMF execution phase when:

1. You can answer **yes** with evidence on at least 4–5 of the 6 PMF self-check questions.
2. The 40% Sean Ellis bar is met (or close — 30%+) within your narrow *who*.
3. Retention curve flattens above zero for paying customers.
4. Organic acquisition is a meaningful share of new customers.
5. The leap of faith is verified by behavior.

Or — when you can answer **no** clearly on 4+ of the 6 — you have a pivot decision to make. (See Stage 07.)

## Required reading

- [`frameworks/pmf.md`](../frameworks/pmf.md) — PMF definition and signals
- [`frameworks/pmf_measurement.md`](../frameworks/pmf_measurement.md) — Sean Ellis, retention curves, organic % math
- [`playbooks/pmf_assessment.md`](../playbooks/pmf_assessment.md) — running the self-check
- [`templates/pmf_survey.md`](../templates/pmf_survey.md) — Sean Ellis survey
- [`templates/retention_dashboard.md`](../templates/retention_dashboard.md)

## Agent partner

- `/ent-pmf-evaluator` — runs the 6-question self-check honestly; pushes back on wishful interpretation; interprets your retention curve (flattening vs. asymptoting); finds the over-performing slice hiding inside your average ("savor the surprise")
