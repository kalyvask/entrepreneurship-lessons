# Stage 05 — MVP Build and Test

> John Vrionis's definition: an MVP is a usable product that either proves your leap of faith or gets a customer to pay you.

A lot of confusion lives in the term MVP. This file clarifies it.

The MVP is not the smallest possible product. It is the **smallest possible product that lets you behave like a real business with a real customer using a real product.** That distinction matters because the MVP is where the most important data of the entire journey gets generated.

You don't reach for an MVP first. You reach for it third — after a concept test and an implementation test. Most teams that "build an MVP" in their first month are building it too early, with too many variables, at too much cost. The course's three-phase validation sequence exists to prevent this:

1. **Concept test** — *would they want this?* — Days
2. **Implementation test** — *would they use this specific design?* — One week (a Knapp sprint)
3. **MVP test** — *will they pay for this real, usable product?* — Weeks to months

This stage covers Phase 3. Phases 1 and 2 are covered in [`playbooks/validation_sequence.md`](../playbooks/validation_sequence.md).

## When you are in this stage

- You have a tested value hypothesis from [Stage 04](04_value_hypothesis.md).
- You ran a concept test and people said "show me what you have."
- You ran an implementation test (or you chose to skip it because the build is under two months) and the design holds up.
- You have not yet built the MVP.

## What "good" looks like at the end of this stage

- A **usable product** in customers' hands.
- A **threshold-passing number of customers** desperate enough to pay (or pre-pay).
- Direct evidence on the **leap of faith** — true, false, or genuinely uncertain (and a clear next test to disambiguate).
- An honest answer to: *Are dogs eating the dog food?* — which leads into [Stage 06 — PMF Measurement](06_pmf_measurement.md).

## Two definitions of MVP held in parallel

You will encounter both. Hold them both. They are complementary, not contradictory.

### Ries (The Lean Startup): the learning MVP

> In Ries's terms: the minimum functionality required to prove the leap-of-faith assumptions that are critical to whether the business succeeds.

The Ries MVP is the smallest possible product that *generates the data you need to falsify the leap of faith.* Could be a video. Could be a landing page with a price. Could be a "concierge" service where you hand-deliver the value before you've built the software.

### Blank (The Four Steps to the Epiphany): the economic MVP

> In Blank's terms: the smallest feature set that will get a customer to pay for it.

The Blank MVP forces an economic threshold — pay matters. A landing page is not a Blank MVP because nothing was sold. The discipline forces you to confront pricing, willingness-to-pay, and friction *as part of the test.*

### The framework's synthesis

Rachleff and Vrionis synthesize the two into a usable product that **either lets you prove your leap of faith OR gets a customer to pay you.** The OR is important. Sometimes one is more important than the other — depending on what your leap of faith is.

For a behavioral leap of faith (will people use this? will they trust this? will they adopt this?), focus on the **usable** part. The Ries spirit.

For a willingness-to-pay leap of faith (will they pay this much? at this point? for this much value?), focus on the **paid** part. The Blank spirit.

Most teams need both. But pick a primary.

## What an MVP is NOT

The vocabulary precision Rachleff hammers on:

- **Not a video.** A video is a concept test. It proves *people would want this if it existed.* It doesn't prove they'd use it.
- **Not a Figma prototype.** A Figma prototype is an implementation test. It proves *this design would work if shipped.* It doesn't prove they'd live with the real thing.
- **Not a landing page with a waitlist.** A landing page is a concept test. Waitlists are not behavioral commitments.
- **Not a slide deck or PRD.** Those are pre-build artifacts. Useful, not the MVP.
- **Not the eventual product.** That's the *whole product* (Moore's term — see [`frameworks/crossing_the_chasm.md`](../frameworks/crossing_the_chasm.md)). The MVP and the whole product are opposites — two ends of a spectrum. Stay in MVP as long as you can.

## The "smallest feature set" discipline

The core constraint of the MVP: every feature that does not directly serve the leap of faith is a feature that adds time, cost, ambiguity, and a way for the test to fail for the wrong reasons.

The exercise:

**1. List every feature you'd want.**
Be honest — include the nice-to-haves, the polish, the integrations, the dashboards.

**2. For each feature, ask: does this directly test the leap of faith?**
If yes, it's in v1.
If no, it goes to v2 (or v∞).

**3. For features that *don't* test the leap of faith but seem necessary, ask: can a human do this for now?**
Concierge MVP — you do the work manually behind the scenes. This is *not* cheating. This is the *highest-fidelity test of value* because you can change the work on the fly and observe the customer up close.

**4. For features that *can't* be human-replaced, ask: is the lightest implementation good enough?**
Often a feature can be built in 1/10th the time if you accept that it'll break, won't scale, and isn't pretty. That's fine pre-PMF. The whole point is *unsustainably good.* You're optimizing for learning, not for scale.

A useful slogan, from Paul Graham: do the things that don't scale. Before PMF, scalability is a future problem. Your MVP should embarrass you slightly — if you're proud of the polish, you probably overbuilt.

## The reduction principle (course-specific)

A specific failure mode worth flagging. The course teaches it explicitly:

> The course's principle: when an early adopter sees one benefit they want bundled with two they don't, they conclude it isn't for them, or that they shouldn't pay full price for things they don't need. Reducing features is the only permitted change to the *what*.

In other words: **too many features in your MVP can be as bad as too few.** Early adopters want a sharp, specific, usable answer to their problem — not a bundle of half-built features that solves their problem 80% and adjacent problems 30%.

If you find your MVP needs to be cut down: cut features. Don't add to compensate. Reducing features is the only permitted *what* change. (Changing the *what* otherwise = restart; see [Stage 07](07_pivot_or_persevere.md).)

## Build mechanics

A working pattern for the build:

### Sprint cadence

**Two-week sprints, with a product review at the end of each.** Borrowed from Lean Startup; Rachleff specifically endorses it as a discovery discipline (not just a product management one).

At each product review:
- What was built since last review?
- What did we learn from customers since last review?
- What's the next-most-important thing to build *or learn?*
- Have we accumulated enough evidence to pivot, persevere, or invest further?

### "Use partners where you must"

If a feature is necessary for the MVP but not core to your value, **use a partner.** Use Stripe for payments. Use OpenAI for LLM. Use Hubspot for the CRM. Use Twilio for SMS. The build is not where you create value — the value is in the specific thing you're testing. Save build hours for that.

### Time-box ruthlessly

The MVP should ship in 1–3 months. Not because it's a hard deadline, but because the longer the build, the more variables compound. Six-month MVPs are a sign that the *what* is too big, the *who* is too vague, or the leap of faith is poorly defined.

If your honest answer is "this is going to take 6 months," go back to Stage 04. Either narrow further, or use partners more aggressively, or pick a different leap of faith to test first.

## The voting exercise (course mechanic)

A diagnostic Rachleff uses. Pick **five carefully selected** desperate-customer prospects. Show them your MVP. Ask each: *"On a scale of 0 to 5, how much do you want this?"*

5 = "I love this."
0 = "Not for me."

The trick: **the number is irrelevant.** Five prospects is too small for statistical significance. What matters is what you *learn* from the conversations.

The deepest answer: **zero yeses can be positive** if the objection is *"that's not possible"* rather than *"I don't want this."* If 5/5 say "it can't be done," you have signal that the demand is there — they just don't believe it. *"That's not possible"* + you've now built it = the value hypothesis just became obvious to them.

If 5/5 say "I don't want this" — that's your kill signal. Go back to Stage 02.

If 2–3 say "I love this" + 2–3 say "not for me" — the more useful question is: *what's different about the segments?* You've stumbled onto a sharper *who.*

## What to measure during the MVP test

This stage is short on measurement because Stage 06 covers it. Two things to track:

**1. Did the leap of faith get tested?**
Did real customers behave in a way that you can attribute (with some confidence) to your hypothesized behavioral assumption? Examples:
- Wealthfront: did users actually allow software to manage their money, behaving differently from how they would with a human advisor?
- Airbnb: did renters sleep in stranger's homes? Did hosts open their doors?
- Anthropic: did engineers preferentially adopt the more responsible AI tool, given the choice?

If the leap of faith test is **ambiguous**, the MVP failed at its primary job. Either redesign the MVP to be more diagnostic, or recognize that you set the leap of faith too broadly.

**2. Are they paying?**
Money is the cleanest signal in the world. Free-tier users behave wildly differently from paying customers. **Get paying customers as early as you can**, even if you're embarrassed by the price. The friction of payment is itself a desperation marker — if they pay, they want it.

For B2B, prepay, signed POs, and pilots-with-conversion-terms all count.
For B2C, paid downloads, subscriptions, or one-time purchases count.

## Common failure modes in this stage

| Failure | What it looks like | Why it kills you |
|---|---|---|
| Overbuilding | 6-month MVP with 15 features | Too many variables; you can't interpret the results |
| Underbuilding | The MVP doesn't actually let customers do the thing | You're testing a concept, not the real product |
| Wrong measurement | "We have 1,000 signups" | Signups are vanity; behavior is signal |
| Pretty product, no use | High polish, low engagement | You optimized for the wrong thing |
| Free tier as test | "Let's see if they use it for free first" | Free use is much weaker signal than paid use |
| Skipping the review cadence | Building heads-down for 3 months | You miss the chance to incorporate evidence |
| Changing the what mid-build | Iterating into a different product | Restart, not pivot — almost certainly fatal |
| Building for the panel, not the test | Adding features advisors suggested | Your panel wasn't your buyer |
| Testing 5 variables in 1 MVP | "We changed pricing, audience, channel, feature set, and onboarding" | When the test fails you have no idea why |

## Exit criteria

You move to [Stage 06 — PMF Measurement](06_pmf_measurement.md) when:

1. You have shipped a usable MVP in the hands of real, paying (or pre-paying) customers.
2. Real behavior — not stated preferences — has tested the leap of faith.
3. You have at least 5 paying customers in your narrow *who* segment.
4. You can articulate what you learned in this build cycle in a sentence or two: *"What we found was X, which means the leap of faith is [confirmed / refuted / still ambiguous]."*

If you don't have at least 5 paying customers despite shipping an MVP, you do not have problem-solution-fit. Go back to Stage 02 or 03.

## A note on building the software itself

This repo tells you **what to build and whether anyone wants it** — the value hypothesis, the leap of faith, the smallest testable wedge. It does not cover **how to build the software well**: code review, QA, security audits, shipping, deployment. That's a different layer, and it matters once you're actually writing the MVP.

For the build layer, point yourself at engineering tooling. [gstack](https://github.com/garrytan/gstack) (Garry Tan, MIT) turns Claude Code into a virtual engineering team — planning review, code review that catches production bugs, browser QA, security audits, and release automation. It runs the *build → review → test → ship* half of the sprint that begins where this repo leaves off.

The handoff: this repo gets you to a scoped MVP that tests your leap of faith; a build-layer toolchain helps you ship it without slop. Keep them distinct — *what to build* is a discovery problem; *how to build it well* is an execution problem, and they need different disciplines.

## Required reading

- [`frameworks/lean_startup.md`](../frameworks/lean_startup.md) — Build-Measure-Learn, MVP definitions
- [`frameworks/pmf.md`](../frameworks/pmf.md) — validation sequence, voting exercise
- [`frameworks/crossing_the_chasm.md`](../frameworks/crossing_the_chasm.md) — MVP vs whole product
- [`frameworks/design_partners.md`](../frameworks/design_partners.md) — for B2B: the 2–5 design partners are your MVP customers
- [`playbooks/validation_sequence.md`](../playbooks/validation_sequence.md) — concept → implementation → MVP
- [`playbooks/mvp_scoping.md`](../playbooks/mvp_scoping.md) — how to decide what's in v1

## Agent partner

- `/ent-mvp-scoper` — given your value hypothesis and leap of faith, helps decide the smallest possible MVP that tests the leap of faith. Pushes back on overbuilding.
- `/ent-design-partners` — for B2B: identify, qualify, and manage the 2–5 design partners who co-create the MVP.
- `/ent-mvp-review` — walks you through a two-week product review: what was built, what was learned, what's next.
