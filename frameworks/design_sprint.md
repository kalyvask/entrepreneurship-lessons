# Design Sprint (Jake Knapp)

> Jake Knapp's design sprint, in one line: a five-day process for answering critical business questions by designing, prototyping, and testing ideas with real customers.

A focused, time-boxed methodology developed at Google Ventures for testing big questions before committing to a long build. Documented in *Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days* (Knapp, 2016).

In the Rachleff/Vrionis framework, a design sprint is the **implementation test** phase — between concept test and full MVP. You've validated that the concept is wanted (concept test). You haven't yet committed to building a full MVP. The design sprint compresses 6 months of build-and-test into 5 days.

Often skipped — but useful when the MVP would take more than 2 months to build, when the cost of being wrong is high, or when you have multiple solution-shape candidates to triage.

## When to run a sprint

- **MVP would take 2+ months to build.** The cost of building the wrong thing is high; a sprint can rule out wrong directions cheaply.
- **You have 2–3 candidate solution shapes** and need to triage.
- **You're not yet sure how the product should work** even though you know the problem.
- **You need to align a team** quickly around what to build.

When *not* to run a sprint:

- You haven't done customer discovery. (A sprint is implementation testing; concept and customer testing should come first.)
- The MVP is small. (If you can build it in 3 weeks, just build it.)
- You're using the sprint to avoid customer conversations. (Sprints test ideas with customers; they don't substitute for customer development.)

## The five-day structure

Knapp's original structure. (Modified versions exist — 3-day "design sprints," 1-day "lightning decisions" — but the 5-day is the canonical form.)

### Monday — Map

**Goal:** define the problem, set the goal, agree on what success looks like.

Activities:
- Long-term goal: what's the ambitious vision?
- Sprint questions: 2–3 specific questions the sprint will answer
- Map the customer journey
- Interview experts (your own team's customer-development findings count)
- Pick a target — one specific moment in the journey that's the focus of the sprint

Output: a problem statement, a target moment, sprint questions.

### Tuesday — Sketch

**Goal:** generate solutions. *Diverge* — many possibilities. *Quietly* — individual work, not group brainstorming.

Activities:
- Lightning demos — review competitors and inspirations
- Sketch individually — 4-step exercise:
  1. Notes (20 min) — capture everything from yesterday and demos
  2. Ideas (20 min) — sketch rough ideas, no judging
  3. Crazy 8s (8 min) — 8 sketch variations of best idea
  4. Solution sketch (30+ min) — three-panel storyboard of the chosen direction

Output: each participant has a detailed solution sketch.

### Wednesday — Decide

**Goal:** pick one solution to prototype. (Or, when sketches converge, pick a combined version.)

Activities:
- Art museum — sketches on the wall, no commentary
- Heat map — dot voting (silent)
- Speed critique — quick discussion of each
- Straw poll — pre-vote
- Decider — one designated decider makes the call
- Storyboard — turn the chosen sketch into a step-by-step storyboard

Output: a single storyboard for the prototype.

### Thursday — Prototype

**Goal:** build a high-fidelity facade. Not a real product. A facade that looks real enough to test.

Activities:
- Choose tools (Figma, Keynote, paper, anything)
- Divide work — Maker, Stitcher, Writer, Asset Collector, Interviewer prep
- Build the storyboard into clickable prototype
- Write the interview script for Friday

**Crucial discipline:** the prototype is *not* engineered. It is *not* connected to a backend. It is *not* functional in any real sense. It is a story you can click through.

Output: a clickable prototype.

### Friday — Test

**Goal:** show the prototype to 5 customers. Watch them try to use it. Learn.

Activities:
- 5 user interviews, 60 min each
- Five-act interview structure: friendly welcome, context questions, intro to prototype, tasks and nudges, debrief
- Team watches from a separate room
- After each interview, the team discusses what they saw

**Why 5 users.** Knapp cites research showing 5 users surfaces 85%+ of usability issues. Beyond 5, returns diminish sharply. The point isn't statistical significance; the point is finding consistent breakdowns.

Output: a clear answer on whether the solution direction works, where it breaks, and what to change before the real build.

## What you learn

A good sprint produces three things:

1. **A go / no-go signal** on the solution direction
2. **Specific breakdowns** in the prototype — *"users couldn't find the X button," "users didn't understand what Y meant"*
3. **Surprise insights** — things you didn't think to test that came up

A bad sprint produces enthusiasm and applause. (The same warning as customer development — see [`frameworks/the_mom_test.md`](the_mom_test.md). If users politely nodded, you learned nothing.)

## How it fits the Rachleff three-phase validation

```
Phase 1: Concept Test          Phase 2: Implementation Test       Phase 3: MVP Test
─────────────────────          ──────────────────────────         ─────────────────
What:  Would they want it?     How should it work?                 Will they pay for it?
Cost:  Hours to days           Days (Knapp sprint = 5 days)        Weeks to months
Tools: Video, landing page,    High-fidelity prototype,            Real, usable product
       follow-me-home, ad,     clickable Figma, user testing       in customers' hands
       waitlist, keyword       (5 users)
       search
```

You can skip the implementation test phase if:
- MVP would take under 2 months
- Concept is simple enough that the design decisions are obvious
- You only have one solution shape candidate

Otherwise, the 5-day sprint costs ~$10k of team time and saves you from a 3-month wrong build. Cheap insurance.

## Common failure modes

| Failure | What it looks like | Fix |
|---|---|---|
| Skipping the sprint to "just build" | "We'll just ship in 2 months" | If MVP is 2+ months, the cost of being wrong is higher than 5 days of testing |
| Sprint becomes brainstorm | Group ideation, big whiteboards | Knapp's discipline: silent sketching, individual work, dot voting |
| No real testing on Friday | Internal team review only | Test with 5 actual customers — that's the whole point |
| Building real product | The prototype is engineered | The prototype is a facade — fast, fake, clickable |
| Testing too early | Sprint with no customer discovery | Sprint is implementation, not customer test. Discovery first. |
| Decider not empowered | Designated decider has no authority | The decider must have actual decision power, not consultation only |
| Sprint goal too vague | "How should our product feel?" | Sprint questions must be specific: "Can users complete X in under 90 seconds?" |

## After the sprint

The sprint is a learning intervention. After it:

- **Update the value hypothesis** with what you learned about the *how*
- **Refine the MVP scope** — sprint usually reveals you can ship less than you thought
- **Plan the MVP build** — see [Stage 05](../stages/05_mvp_build.md)
- **Carry the storyboard forward** — it becomes the product spec

## Where this lives in the journey

- [Stage 05 — MVP Build](../stages/05_mvp_build.md) — sprint is the implementation-test phase before MVP
- [`playbooks/validation_sequence.md`](../playbooks/validation_sequence.md) — concept → implementation → MVP

## Source

*Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days* — Jake Knapp with John Zeratsky and Braden Kowitz (Simon & Schuster, 2016). Developed at Google Ventures. Knapp's writing and the GV website are good supplementary resources. Adopted in the PMF framework as the recommended implementation-testing methodology.
