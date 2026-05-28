# The Three-Phase Validation Sequence

Rachleff's discipline for validating a value hypothesis. The sequence runs concept test → implementation test → MVP test, each cheaper to run and more rigorous than the next. **Skip a phase only when you're confident the data from a prior phase makes the next one unambiguous.**

## Why three phases

The discipline exists because **one big test (the MVP) confuses too many variables.** You build for 3 months. The results are ambiguous. You don't know if the leap of faith was wrong, the implementation was wrong, the pricing was wrong, or the audience was wrong.

By front-loading cheaper tests (concept, then implementation) before the expensive one (MVP), you isolate variables. By the time you get to MVP build, you've already eliminated the failures that didn't require a build.

## The three phases

| Phase | Question it answers | Tools | Cost | Time |
|---|---|---|---|---|
| **Concept test** | Would they want this? | Video, landing page, follow-me-home, smoke test, keyword search | Hours to days | Days |
| **Implementation test** | Would they use this *specific design?* | High-fidelity prototype, Figma, Knapp 5-day sprint | Days to weeks | 1 week |
| **MVP test** | Will they pay for / use the real product? | Usable, paid, real product | Weeks to months | 1–3 months |

## Phase 1 — Concept test

**Goal:** can you find evidence that someone *would want* what you're proposing, *if it existed*?

### The discipline

You are not validating a feature list. You are testing the **core value proposition** — that the *what / who / how* you described in Stage 04 would be wanted by the customer.

The cost should be **days, not weeks.** A concept test that takes 3 weeks to build is too expensive — you're effectively running an implementation test.

### Specific concept-test formats

- **Smoke test landing page** — a landing page with the value prop and a "join waitlist" or "pre-order" button. The number of people who click is the test. (Note: waitlist signups are *weak* signal — see "what NOT to count" below.)
- **Dropbox video** — short video explaining the product as if it existed. Drew Houston's Dropbox MVP. Demand signal: video views, signups, social shares.
- **Concierge** — you manually do the work behind the scenes. The customer sees the result; they don't know there's no software yet. (Food on the Table started this way.)
- **Wizard of Oz** — what looks like AI is a human responding to prompts. Customer thinks it's automated.
- **Follow-me-home** — you go to the customer's workplace and walk through their day. You observe where the proposed product would fit, what's broken about their current process, what they'd react to.
- **Keyword search demand check** — Google Keyword Planner, SEO tools. Are people searching for this problem? At what volume?
- **Ad test** — run a paid ad to a landing page that describes the product. CPC + conversion rate tells you whether the message resonates and the offer pulls.

### What counts as a positive signal

- **Real money committed** — pre-payment, deposit, signed LOI
- **Real time committed** — willingness to take a follow-up demo, signing up for a beta with explicit terms
- **Strong behavioral commitment** — completing a multi-step signup or onboarding when the product doesn't exist
- **Spontaneous referrals** — they share the landing page with peers without being asked

### What does NOT count

- ❌ Waitlist signups without further commitment
- ❌ "Looks interesting" responses
- ❌ Form submissions for a free trial they may or may not use
- ❌ Survey responses (especially "would you use this?" — stated future intent is noise)
- ❌ Click-through rates on ads (without action behind them)

### When to skip Phase 1

- You're already deep in RDI / customer discovery and have many desperate-customer commitments
- The customer is already pre-paying based on a verbal pitch

Otherwise: don't skip. Phase 1 is the cheapest learning you'll do.

## Phase 2 — Implementation test

**Goal:** would they use this *specific design*?

You've established that they'd want it. Now: when you show them how it would work, would they actually adopt it? Or would the workflow / UX / mental-model be wrong?

### When to run Phase 2

- The MVP would take **2+ months** to build
- You have **2–3 candidate solution shapes** and need to triage
- The cost of being wrong on design is high (you're building an enterprise integration, a hardware product, a tool that requires onboarding)

### When to skip Phase 2

- The MVP build is **less than 2 months**. The design questions are answered fast enough by building.
- The concept is mechanically obvious (a small marketplace, a simple data import-export tool, etc.)
- You only have one solution shape candidate

### Specific implementation-test formats

- **Knapp 5-day design sprint** — the canonical form. See [`frameworks/design_sprint.md`](../frameworks/design_sprint.md).
- **Clickable Figma prototype** — a high-fidelity facade. Built fast, fake. Tested with 5 customers.
- **Concierge with detailed workflow** — like a concept test but explicit about *how* the customer would use it
- **Spec document with sketches** — for technical buyers, a detailed PRD with mocks. Customer responses to specific design choices.

### What counts as a positive signal

- Customer **completes the task** in the prototype without significant confusion
- Customer **understands the value** within first 60 seconds
- Customer **anticipates the next step** correctly
- Customer **describes how they'd use it** in their own words
- **Specific feedback on improvements** that doesn't change the core direction

### What does NOT count

- Customer says "yeah, this is cool"
- Customer "loves the design"
- No specific tasks completed

The implementation test is **not** a usability study in the traditional sense. It is a **strategic validation** — does this design solve the job in a way the customer will adopt?

## Phase 3 — MVP test

**Goal:** prove the leap of faith and/or get customers to pay.

The MVP is the most expensive test — weeks to months of engineering. By the time you reach here, Phase 1 and 2 should have eliminated the obvious failures.

See [Stage 05 — MVP Build](../stages/05_mvp_build.md) for the full operational guidance.

### What counts as a positive signal

- 5+ paying customers in your narrow *who*
- Retention curve flattens above zero
- Customers refer without being asked
- Sales cycles shorten
- The leap of faith is verified by behavior

### What does NOT count

- Signups
- Trial users without conversion
- Press coverage
- Investor interest

## Decision points between phases

After each phase, three options:

**Persevere** — the data confirms the hypothesis (or is strongly positive). Move to next phase.

**Pivot** — the data contradicts a specific element. Common pivots between phases:
- *After Phase 1:* concept test fails → narrow the *who* (the problem is real but not for this segment) or refine the messaging (positioning is off, value not understood)
- *After Phase 2:* implementation test fails → simplify the design, or test a different solution shape
- *After Phase 3:* MVP fails → see [Stage 07 — Pivot or Persevere](../stages/07_pivot_or_persevere.md)

**Kill** — the data shows there's nothing here. The problem doesn't exist for this segment, or the proposed solution genuinely doesn't fit the job. Better to know now than after 6 more months.

The decision between Phase 1 and Phase 2 is usually fast (hours to days of debrief). The decision after Phase 3 is usually slower — months of running and measurement.

## Worked example

A team exploring software for mid-market vertical farms:

**Phase 1 — Concept test:**
- Built a landing page with value prop + "request a pilot" CTA
- Ran small ($500) LinkedIn ad targeting "farm manager" titles in CEA
- Result: 8 click-throughs, 2 requests for demos, 1 willingness to pre-pay
- *Verdict:* concept resonates with the narrow *who*; proceed to implementation

**Phase 2 — Implementation test (Knapp sprint, 5 days):**
- Built clickable Figma prototype of the daily-harvest scheduling flow
- Tested with 5 farm GMs (3 from concept-test pipeline + 2 from referrals)
- 4 of 5 completed the core task without prompt; 3 of 5 anticipated next step
- 2 explicit asks: "Can it integrate with my Argus system?" and "How does it handle two delivery windows in one day?"
- *Verdict:* core design works; refine the Argus-integration scope before MVP

**Phase 3 — MVP test:**
- 3-month build (paid pilot with 2 customers; 1 free pilot)
- After 4 months of usage: 1 churned, 2 retained and using daily
- 1 referral generated; both retained customers paid a 30% pricing increase without pushback
- *Verdict:* approaching PMF in this narrow segment; double down on this *who*; scale outbound to similar farms

In retrospect, Phase 1 and 2 saved this team from a likely 3-month wrong build that would have spent capital on the wrong integration scope and the wrong workflow.

## Common failure modes

| Failure | What it looks like | Fix |
|---|---|---|
| Skipping Phase 1 | "Let's just build the MVP" | Run a landing page first; the day of work saves months |
| Concept test as a survey | Asking "would you use this?" | Use behavioral signals: pre-payment, time commitment |
| Mistaking signups for signal | "We got 1000 waitlist signups" | Signups without further commitment are noise |
| Phase 2 with no Phase 1 | Building a Figma prototype without confirming demand | Sequence matters — demand first |
| MVP test confounded by 5 variables | Changing pricing, audience, channel, features, design simultaneously | Hold variables fixed; change one at a time |
| Building a perfect Phase 2 | A polished prototype that took 3 weeks | Phase 2 is fake; speed > polish |
| Walking away from a single negative Phase 1 | "Nobody clicked the ad; the idea is dead" | Run multiple tests with multiple messages — one ad isn't enough |

## Where this lives in the journey

- [Stage 03 — Problem-Solution Fit](../stages/03_problem_solution_fit.md) — Phase 1 concept test
- [Stage 04 — Value Hypothesis](../stages/04_value_hypothesis.md) — articulated before Phase 1
- [Stage 05 — MVP Build](../stages/05_mvp_build.md) — Phase 2 and 3
- [`frameworks/design_sprint.md`](../frameworks/design_sprint.md) — Phase 2 specifics
- [`frameworks/pmf.md`](../frameworks/pmf.md) — overall validation discipline

## Source

Synthesized from Andy Rachleff's framework (validation as concept→implementation→MVP sequence); Jake Knapp's *Sprint*; Steve Blank's customer development.
