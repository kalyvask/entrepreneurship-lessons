# The 10-Star Product (and Scope Modes)

> Brian Chesky's lens for designing delight at Airbnb: imagine the experience several stars beyond five, all the way to an absurd 11-star version, to surface improvements you'd never reach by aiming for "good."

A lens for **setting ambition** — and then deliberately deciding how much of that ambition to build right now. It pairs with this repo's narrowing discipline: the 10-star vision tells you the *ceiling* (is this worth ten years?); the narrowest wedge tells you the *floor* (what do I test this week?). You need both, and they pull in opposite directions on purpose.

## The 11-star experience (Chesky)

Brian Chesky's framework for designing Airbnb's guest experience. Imagine the experience on a star scale, and keep going past the realistic:

- **5 stars** — you arrive, the host greets you, you check in. You got what you expected. (Most companies stop designing here.)
- **6 stars** — the host knows your name, has your favorite snacks waiting.
- **7 stars** — a car is waiting for you at the airport.
- **8 stars** — you arrive to a welcome event tailored to why you're in town.
- **9 stars** — ...
- **10 stars** — you're met at the airport by a parade in your honor.
- **11 stars** — you step off the plane and Elon Musk is there to take you to space.

The 11-star experience is **absurd and unbuildable on purpose.** That's the point. By imagining the extreme, you surface the realistic 6-, 7-, 8-star improvements you'd never have thought of while aiming for "good." Then you **walk it back** from the absurd to the shippable — and you ship something more delightful than you'd have designed by aiming for 5.

**The move:** dream the absurd version to find the delight, then walk back to what you can actually build.

## Why founders need this

Two failure modes the 10-star lens guards against:

1. **Aiming for "good."** If you design for 5 stars (meets expectations), you build something forgettable. Forgettable products don't generate the word-of-mouth that signals PMF (see `frameworks/pmf.md` — organic growth requires *desperation* and *delight*, not adequacy). The 10-star exercise forces you past "good enough."

2. **Building the absurd version.** The opposite failure: falling in love with the 11-star vision and trying to build all of it before testing anything. That's a multi-year project with five untested assumptions baked in. (See `stages/05_mvp_build.md` on why this is fatal.)

The discipline is to **hold both**: know the 10-star vision (so your ambition and your narrative are big enough to be worth a decade) *and* ruthlessly narrow the first move (so you actually learn).

## The four scope modes

Once you can see the 10-star vision, you have to decide — for *this* decision, *this* sprint, *this* release — how far toward it to build. Four deliberate modes (adapted from gstack's CEO-review framing):

### Expansion
**Go bigger.** The request is too small; the real opportunity is larger. You're under-reaching. Use when: the market rewards ambition, you've found a 10-star vision worth chasing, and the narrow version wouldn't be differentiated. *Rare pre-PMF.*

### Selective Expansion
**Bigger on the dimensions that matter, narrow on the rest.** Expand the one or two things that create delight or defensibility; hold everything else tight. Use when: there's a specific 10-star dimension (the magical moment) that's worth investing in, but the rest can stay minimal.

### Hold Scope
**Resist the creep.** The scope is right; the temptation is to add. Use when: you've defined a good wedge and stakeholders (or your own excitement) keep trying to expand it. The discipline is to *say no* and ship what you scoped.

### Reduction
**Cut to the core.** The scope is too big; strip it to the leap of faith. Use when: pre-PMF (almost always), the build is sliding past 3 months, or the MVP has accumulated features that don't test the core assumption. **This is the default mode before PMF.**

## How to use it

A working sequence at the idea/insight stage (Stage 01) and again before each build (Stage 05):

1. **Run the 10-star exercise.** What's the absurd, delightful, extreme version of this product? Don't censor. (This also tests whether the vision is worth ten years — if the 10-star version doesn't excite you, find a different idea.)
2. **Extract the delight.** What 6-, 7-, 8-star improvements did the extreme reveal that you'd have missed?
3. **Pick the scope mode for the current move.** Pre-PMF, default to **Reduction** — strip to the narrowest wedge that tests the leap of faith. Use **Selective Expansion** only for the single magical-moment dimension if there is one.
4. **Define the wedge.** The narrowest version you can put in front of a desperate customer this week (see `stages/05_mvp_build.md` and `/ent-mvp-scoper`).
5. **Keep the 10-star vision in the narrative, not the v1 build.** Investors and recruits buy the 10-star vision; customers buy the working wedge. Both are true at once.

## The tension with narrowing — resolved

This repo hammers *narrow, narrow, narrow* (the Wealthfront staircase, the narrowest wedge, the single leap of faith). The 10-star lens seems to pull the other way — *dream bigger*. The resolution:

- **Vision: 10-star.** The future you're building toward should be ambitious enough to be worth a decade and to generate genuine delight. A small vision produces a forgettable product.
- **First move: narrowest wedge.** What you build and test *first* should be the smallest slice that proves your leap of faith.
- **The bridge: the wedge is a credible path to the vision.** The narrow first move isn't a small ambition — it's the beachhead (see `frameworks/crossing_the_chasm.md` — bowling pins) from which the 10-star vision becomes reachable.

Rachleff's point that you should aim for a $100M business because it takes about the same work as a $5M one is the same idea: dream big on the destination, narrow hard on the first step.

## Common failure modes

| Failure | Why it kills you |
|---|---|
| Designing for 5 stars | Forgettable product; no delight; no word-of-mouth; no PMF signal |
| Building the 11-star version | Multi-year project, five untested assumptions, no learning |
| No scope mode chosen | You drift — usually toward Expansion via feature creep |
| Expansion mode pre-PMF | Adding scope before validating the core is the classic capital-burn |
| 10-star vision that doesn't excite you | If the destination is "meh," you won't survive ten years; find another |
| Confusing vision with v1 | Telling customers the 10-star story when the product is a 5-star MVP |

## Where this lives in the journey

- [Stage 01 — Insight and Idea](../stages/01_insight_and_idea.md) — set the 10-star vision; test whether it's worth a decade
- [Stage 04 — Value Hypothesis](../stages/04_value_hypothesis.md) — the wedge is the value hypothesis; the vision is the narrative
- [Stage 05 — MVP Build](../stages/05_mvp_build.md) — default to Reduction; ship the narrowest wedge
- [`frameworks/pmf.md`](pmf.md) — narrowing discipline, "aim for $100M"
- [`frameworks/crossing_the_chasm.md`](crossing_the_chasm.md) — the wedge as beachhead toward the vision
- The `/ent-office-hours` skill uses this lens to reframe a request and recommend the wedge

## Source

The 11-star experience is Brian Chesky's (Airbnb), told on Reid Hoffman's *Masters of Scale*. The four scope modes (Expansion / Selective Expansion / Hold Scope / Reduction) are adapted from Garry Tan's gstack `/plan-ceo-review` (MIT-licensed). Synthesized here with this repo's narrowing-and-wedge discipline.
