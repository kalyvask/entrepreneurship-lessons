# Stage 03 — Problem–Solution Fit

> *"All the value lies in the surprise. When you find one, drop everything and focus solely on it."* — Scott Cook, Intuit

Problem–Solution Fit is the bridge stage. By the end, you should be able to claim:

- **The problem is real** — a specific group of people exhibit desperation around it.
- **A solution is plausible** — you have an idea, however rough, of what to build that addresses the desperate pain.
- **The economics could work** — even on a back-of-the-envelope, the unit economics aren't structurally broken.

This stage is short — typically 2–4 weeks. It is mostly about deliberately taking your customer discovery output and turning it into a defensible problem statement plus a candidate solution shape, before you commit to spending months building.

It is *not* PMF. PMF requires actual customers using actual product. Problem–Solution Fit just means **the problem is worth solving, and a solution worth building.**

## When you are in this stage

- You finished [Stage 02 — Customer Discovery](02_customer_discovery.md) with a desperate customer segment and a recurring problem pattern.
- You have not yet locked in the full value hypothesis (Stage 04) or designed an MVP (Stage 05).
- You are running 1–2 weeks of concept tests to sharpen the solution shape.

## What "good" looks like at the end of this stage

- A **problem statement** in a single sentence: *who* is desperate for *what relief* from *what pain*.
- A **draft solution shape** — not a feature list, but the rough functional answer to the problem.
- A **rough unit economics calculation** showing the math isn't structurally broken (LTV/CAC plausible, gross margin healthy at scale, no obvious cost-of-goods or sales-cycle landmines).
- A **whittle of the original alternatives list** — which existing alternatives your solution beats, on what dimensions, and which it doesn't (and why those customers may be a different segment).
- An **explicit list of risky assumptions** that you'd need to test before building.

## The three tests this stage runs

### Test 1: The problem is real, hot, and recurring

This was substantially answered in Stage 02. But the move at this stage is to **make it explicit and falsifiable.**

Take everything you have from discovery and write it down in this shape:

```
PROBLEM STATEMENT
The desperate customer: [one sentence — narrow enough to identify 50 of them]
The pain: [a single, specific pain — not a list]
The trigger: [what event or situation causes the pain to flare]
Frequency: [how often does this happen — daily, weekly, quarterly]
Magnitude: [what does it cost them when it happens — time, money, opportunity]
Current alternatives: [what they do today — including DIY, workarounds, doing nothing]
Why those alternatives fail: [structural reason — not "they're bad", but "they require X that doesn't exist"]
Evidence of desperation: [3+ concrete behavioral signals from real conversations — name names if you can]
```

If you can't fill this in cleanly, the problem isn't ready. Go back to Stage 02 for more conversations or pick another candidate problem from your insight.

### Test 2: A solution is plausible

This is *not* designing the product. It is sketching a **solution shape** — the functional answer to the problem. Concrete enough to evaluate, abstract enough that you're not committing to specific features yet.

A good solution shape:

```
SOLUTION SHAPE
What it is: [one sentence — what kind of thing is this. Software? Service? Device? Platform?]
What it does for the customer: [the job it's hired for — not the features]
How it's used: [the rough usage pattern — daily? episodic? embedded?]
What makes it differ from the alternatives: [the change vector that makes this possible now]
What would have to be true for this to work: [the leap of faith — the one thing that has to be right]
What it's NOT: [explicit exclusions — these prevent feature creep later]
```

Sketch 2–3 candidate solution shapes. Talk to 5–10 of your desperate customers about each. Use concept tests, not pitches (see [Stage 06 — Validation](06_pmf_measurement.md) for the full three-phase test sequence: concept → implementation → MVP).

A **concept test** is a Dropbox-style video, a landing page that explains the idea, a sketched flow on paper, or a "follow-me-home" conversation where you walk through how they'd use it. The cost: hours, not weeks. The output: does the customer light up, or politely nod?

### Test 3: The economics aren't structurally broken

You do not need a financial model in this stage. You need a **structural check** that says *if this works mechanically, the math could be okay.*

The check has four numbers (rough, order-of-magnitude):

- **Willingness to pay (WTP):** What would a desperate customer pay? Get a triangulation: existing alternatives × pain magnitude × budget reality. *Not what they say — what they *behave* like in pricing conversations.*
- **Cost to deliver:** What does it cost to deliver this once? Cost of goods, infrastructure, support, success motion.
- **Cost to acquire (CAC):** How would you reach a customer? Outbound? Inbound? PLG? Channel? Rough cost per closed account.
- **Repeat / retention:** Will they keep using and paying, or is it a one-time purchase? Affects LTV dramatically.

Rough LTV/CAC plausibility test: *LTV / CAC > 3 at scale, with payback < 12 months* is healthy. If your back-of-envelope says LTV/CAC < 1, the business is structurally broken — even with PMF, you'll lose money on every sale. That's a problem you need to solve in this stage by changing pricing, channel, or who you're selling to.

**This is not financial planning. This is sanity checking.** A high LTV/CAC on the back of the envelope doesn't mean it'll work; a low one means it definitely won't.

See [`frameworks/unit_economics.md`](../frameworks/unit_economics.md) for the calculation.

## "Savor the surprise"

A phrase from Scott Cook of Intuit, central to the PMF framework. Some of the most important learning in this stage comes from **what surprises you in conversations** — not what confirms you.

Specifically:
- A workaround a customer described that you'd never imagined.
- A subset of customers who behave 3× differently from the rest.
- A pricing reaction you didn't predict.
- A pain that came up unprompted in 7 of 12 conversations but wasn't in your hypothesis.

When you find a surprise: **drop other initiatives. Probe it.** This was true for Airbnb (the professional-photo conversion rate); it'll be true for you in smaller ways.

Surprises are how you upgrade the *what* without restarting — you keep the original insight, but you sharpen the solution shape with information you couldn't have planned for.

## Common failure modes in this stage

| Failure | What it looks like | Why it kills you |
|---|---|---|
| Jumping to MVP before validating shape | "Let's just build it" | You'll spend 3 months building the wrong thing |
| Falling in love with one solution shape | Only sketching 1 candidate | Survivorship bias: you only get evidence for the one you picked |
| Hypothetical pricing tests | "Would you pay $50/month for this?" | Stated WTP is unreliable; you need pricing pressure from real conversations |
| Skipping the unit economics check | "We'll figure pricing later" | If LTV/CAC < 1 at scale, you can't fix it with growth |
| Building a feature list instead of a solution shape | Pages of bullets | Premature concretization — locks you into specifics before you've earned the right |
| Treating "they liked the concept" as validation | Nodding in a 30-min call | Concept-test "yes" is necessary but not sufficient; you need behavior commitment (signed LOI, prepay, etc.) |
| Ignoring deal-breakers | "Yes, but their legal will never approve this" → you build anyway | If the deal-breaker is structural, no amount of product polish fixes it |

## Exit criteria — leaving this stage

You move to [Stage 04 — Value Hypothesis](04_value_hypothesis.md) when:

1. The problem statement is filled in cleanly and you can defend each line with evidence.
2. You have selected one solution shape (with one or two alternates on file).
3. Concept testing has produced *behavioral commitments* from 3+ desperate customers — they'd pre-pay, sign LOIs, or sketch a launch plan with you.
4. The unit economics pass the back-of-envelope check (LTV/CAC > 3 at plausible scale, payback < 12 months, gross margin healthy).
5. You can name your leap of faith — the one thing that has to be true.
6. You can list 3–5 risky assumptions you'd need to test before building.

If you can't get to all of these in 4 weeks, look hard at what's missing. Sometimes the answer is *the original insight wasn't sharp enough* and you need to go back to Stage 01.

## Required reading

- [`frameworks/pmf.md`](../frameworks/pmf.md) — leap of faith, value hypothesis
- [`frameworks/unit_economics.md`](../frameworks/unit_economics.md) — back-of-envelope checks
- [`frameworks/design_partners.md`](../frameworks/design_partners.md) — for B2B: identify design-partner candidates now
- [`playbooks/concept_test.md`](../playbooks/concept_test.md) — running concept tests cheaply
- [`templates/problem_statement.md`](../templates/problem_statement.md)
- [`templates/solution_shape.md`](../templates/solution_shape.md)

## Agent partner

- `/ent-problem-statement` — turn your discovery notes into a defensible problem statement
- `/ent-concept-test` — design a concept test for a candidate solution shape
- `/ent-design-partners` — identify and qualify design-partner candidates (B2B)
- `/ent-unit-econ-check` — back-of-envelope LTV/CAC sanity check
