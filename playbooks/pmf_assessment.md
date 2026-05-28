# PMF Assessment Playbook

A structured, honest self-check for product-market fit. Run quarterly during MVP testing and growth.

The honest answer is almost always *"not yet."* The discipline is in admitting it cleanly.

## The PMF self-check — 6 questions

Run these in order. Answer each with evidence, not feeling.

### Question 1 — The narrow *who*

**Have we held the *who* narrow, or have we broadened to accommodate the customers we got?**

If you broadened: the customers you've added are likely contributing noise. Reset to the original narrow *who* and measure only against those customers.

**Test:** of the customers you have, how many are in your originally-defined narrow *who*? Of those, how many are paying, retained at 12 weeks, and using weekly?

If the answer is fewer than 5: you don't yet have a customer base in your target segment. PMF assessment is premature.

### Question 2 — The leap of faith

**Is the behavioral assumption verified? Yes / No / Ambiguous?**

If verified: by what specific behavior, not by general enthusiasm?

If ambiguous: was the MVP not diagnostic enough? Did you bake too many variables into one test?

**Test:** can you write a one-paragraph description of *what customers actually did* that confirmed (or refuted) the leap of faith? Specific behaviors, dates, numbers — not impressions.

### Question 3 — Retention curve

**Plot the weekly retention curve by cohort.**

- Where does it stabilize?
- Is the curve improving cohort over cohort?
- For paying customers (not free) specifically: same questions.

**Test:** does the curve **flatten above zero**, or does it asymptote to zero?

Flattens above zero = strong signal.
Asymptotes to zero = no PMF, regardless of revenue.

### Question 4 — Organic acquisition

**Trend the % of new customers from organic channels over the last 6 months.**

Organic = referral, direct, organic search, word-of-mouth, organic social, press, unpaid.

- Is it climbing, flat, or declining?
- Could you stop paid acquisition tomorrow and still grow? (At PMF, the answer is usually yes.)

**Test:** **organic % > 40%** of new customers in the recent month? Climbing trend over the prior 6?

### Question 5 — Sean Ellis test

**Run it on active users in the narrow *who*.**

The question: *"How would you feel if you could no longer use [product]?"*

Options:
- Very disappointed
- Somewhat disappointed
- Not disappointed (it isn't really that useful)
- N/A — I no longer use [product]

**Test:** **40%+ of active users say "Very disappointed."**

Most pre-PMF startups land at 10–25%. Climbing the curve from there means narrowing the *who* and serving them better.

After running the survey: **read the comment box of the "very disappointed" cohort.** Their reasons should describe the desperation markers (see [`frameworks/rachleff_pmf.md`](../frameworks/rachleff_pmf.md)).

### Question 6 — The "tell" tests

**Behavioral signals beyond the metrics:**

- Do customers refer without being asked?
- Do customers demand features in a way that says "I depend on this product"?
- Are sales cycles shrinking? Has the friction of getting a new customer dropped?
- Do you have inbound interest you didn't generate?
- Customers volunteer to sell your product? (Vrionis's tell.)
- Pricing power — could you raise prices on new customers without losing them?

**Test:** are at least 3 of these YES?

## Scoring

| Score | Interpretation |
|---|---|
| **6 / 6** | You have PMF. Move from search to scale. |
| **4–5 / 6** | Approaching PMF. Identify the failing dimensions; **enhance the good**, don't fix the bad. |
| **2–3 / 6** | Real signal in some places; pivot the *who* or *how* to consolidate. |
| **0–1 / 6** | No PMF. Pivot (or shut down) — see [Stage 07](../stages/07_pivot_or_persevere.md). |

The scoring is rough. The discipline is in actually answering all 6 honestly.

## What does NOT count

A list, because every team gets seduced by at least one:

❌ Revenue growth alone — paid acquisition masks the truth
❌ Signups / waitlists
❌ Trial conversions without retention
❌ Investor enthusiasm pre-PMF
❌ Press coverage
❌ Hiring growth
❌ "We're in 50 countries"
❌ Customer logos without active retention
❌ "Our biggest customer loves us" (anecdote, not market)

## Specific signals to look for

### Strong PMF signals

- The Sean Ellis 40% bar is met
- Retention curve plateaus
- Organic acquisition is 40%+ and climbing
- Sales cycles are shrinking
- Customers refer unsolicited
- Pricing power exists (you can raise prices)
- The team feels like they're running, not pushing
- Investors come to you, not the other way around (lagging signal)

### Soft PMF signals (necessary but not sufficient)

- Customers say things like "this changed how we operate" unprompted
- Specific use frequency above the modeled rate
- A small number of customers using the product in unexpected ways
- Active discussion on whatever channel they hang out on (Slack, Discord, etc.)

### Anti-signals (you probably don't have PMF)

- Paid acquisition is climbing but retention is asymptoting to zero
- The customer base has broadened beyond the narrow *who*
- Each renewal feels like a negotiation
- Every win is hard-fought
- You're not sure who's most desperate among your customers
- Your customer base is diverse but no single segment is desperate

## Diagnosing why you don't have PMF

If you scored 0–3 / 6, the failure mode points toward the pivot direction:

```
Q1 + Q2 fail (wrong narrow who, leap of faith ambiguous)
   → Pivot the WHO

Q1 OK but Q5 fails (right segment, Sean Ellis low)
   → Narrow further; the segment is too broad

Q3 fails (retention asymptotes)
   → The product solves a one-time job, not an ongoing one
   → OR the customer base is mostly non-desperate; narrow the WHO

Q4 fails (no organic growth)
   → Either the customer isn't talking about it (low desperation)
   → OR the distribution is broken (pivot the HOW)

Q6 fails (no "tells")
   → Likely you're in approaching-PMF territory but not there yet
   → Persevere if other signals are improving cohort over cohort
```

## "Enhance the good" vs "Fix the bad"

A specific course principle for what to do when you're 50–75% of the way to PMF:

**The course's principle: enhancing the good improves growth. Fixing the bad almost never does.**

The intuition: the customers you didn't get were not desperate. The customers you did get were. Investing in the desperate ones — making the product better for them, finding more of them — is how you accelerate. Trying to convert the indifferent ones is fighting their nature.

**When approaching PMF:** find the over-performing slice in your data (the cohort that retains at 80%; the customer who refers 10 others; the segment that uses 10× more than average). That's where PMF lives. Find more of them. Serve them deeper.

## The PMF status memo

To yourself and your team. Honest format:

```
PMF STATUS — [Date]

In our narrow who segment ([segment name], N=[number of active customers]):

1. Holding narrow who?              [Yes / Broadened to include X]
2. Leap of faith verified?          [Yes (by behavior X) / No / Ambiguous]
3. Retention curve shape:           [Flattens at X% week 12 / Asymptotes to zero]
4. Organic % new customers:         [X%] — trend: [climbing / flat / declining]
5. Sean Ellis "very disappointed":  [X%] (N=[active users surveyed])
6. Tells:                           [List the ones that apply]

PMF score:                          [X / 6]

Verdict: [PMF / approaching PMF / not yet / need to pivot]

Most important action this quarter: [specific, time-boxed, single most important thing]
```

If you cannot fill this in cleanly, you do not yet have PMF *or* the data to claim it.

## Common failure modes

| Failure | Why it's a problem |
|---|---|
| Running the assessment on inactive users | Inactive users distort everything |
| Running on all customers (not narrow who) | The narrow who is where signal lives |
| Wishful interpretation of weak retention | "It'll plateau eventually" — it won't |
| Counting paid acquisition as growth | Paid masks the truth |
| Anecdote over data | "Our biggest customer loves us" ≠ market signal |
| Sean Ellis survey too small (N<30) | Individual responses dominate; statistically meaningless |
| Skipping the Sean Ellis comments | The number alone is much less informative than the reasons |
| Refusing to score 0–1 honestly | If you can't admit non-PMF, you'll never pivot in time |

## Where this lives in the journey

- [Stage 06 — PMF Measurement](../stages/06_pmf_measurement.md) — primary use
- [Stage 07 — Pivot or Persevere](../stages/07_pivot_or_persevere.md) — if score is low
- [`frameworks/pmf_measurement.md`](../frameworks/pmf_measurement.md) — Sean Ellis, retention curves, organic math
- [`templates/pmf_survey.md`](../templates/pmf_survey.md) — Sean Ellis survey template

## Source

Sean Ellis test by Sean Ellis. Retention curve discipline from broad startup analytics (Brian Balfour, Lenny Rachitsky). Rachleff's PMF framework. The "enhance the good" principle is Rachleff's reformulation of "savor the surprise" (Scott Cook).
