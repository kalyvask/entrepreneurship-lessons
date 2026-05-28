# Concept Test Playbook

The first and cheapest phase of validation: **prove that someone would want what you'd build, before you build it.** Days, not weeks. (See the full three-phase sequence in [`playbooks/validation_sequence.md`](validation_sequence.md).)

A concept test does NOT validate that people will *use* a specific design (that's the implementation test) or that they'll *pay for and retain* a real product (that's the MVP test). It validates the **core value proposition**: that the *what / who / how* from your value hypothesis is wanted by the desperate customer.

## The discipline

You are testing the value proposition, not collecting opinions. The output you want is **behavioral commitment**, not encouragement. (See [`frameworks/the_mom_test.md`](../frameworks/the_mom_test.md).)

A concept test should cost **days, not weeks.** If it takes three weeks to build, you've drifted into building an implementation test (or an MVP) — stop and simplify.

## The formats

Pick based on your customer and what's fastest to put in front of them.

### Smoke-test landing page

A landing page that explains the value proposition with a clear call to action ("request access," "pre-order," "book a pilot"). Drive a small amount of targeted traffic (a $200–500 ad, a LinkedIn post, a few warm intros).

- **Measures:** click-through, then *what they do next* (the real signal is the post-click action, not the click).
- **Build time:** hours (Carrd, Framer, a single HTML page).
- **Strong signal:** they fill out a qualification form, book a call, pre-pay, or sign an LOI.
- **Weak signal:** waitlist signup with no further commitment.

### Explainer video (the Dropbox MVP)

A short video showing the product as if it existed. Drew Houston's original Dropbox video had no working product behind it — it tested whether the concept resonated. Demand signal: views, signups, shares, comments.

- **Build time:** a day or two.
- **Best for:** products that are hard to prototype but easy to *show* the value of.

### Concierge

You manually deliver the value, by hand, behind the scenes. The customer experiences the outcome; they don't know there's no software yet.

- **Build time:** zero build — you do the work.
- **Strong signal:** they pay for the manual version, come back for more, refer others.
- **Bonus:** you learn exactly what the product needs to do by doing it yourself. The best spec comes from being the concierge.

### Wizard of Oz

What looks automated is actually a human responding. The customer interacts with what seems like a finished product; you're pulling the levers manually.

- **Best for:** testing whether the *interaction model* works before building the automation.

### Follow-me-home

You go to the customer's actual workplace (or screen-share through their actual workflow) and watch them do the job today. Then you walk through how your concept would fit.

- **Strong signal:** they get visibly excited about where it would slot in; they describe how they'd use it unprompted; they ask "when can I have it?"
- **Bonus:** you see the real workflow, the real workarounds, the real constraints — things they'd never tell you in an interview.

### Keyword / demand check

Use Google Keyword Planner, search volume tools, or ad-impression data to gauge whether people are actively searching for the problem or solution.

- **Best for:** a quick read on whether latent demand exists before you invest in anything.
- **Caveat:** search demand validates *awareness of the problem*, not desperation. Pair it with conversations.

## What counts as a positive signal

The bar is **behavioral commitment** — something that costs the customer time, money, or reputation:

- 🟢 Pre-payment, deposit, signed LOI
- 🟢 Booking a real pilot with terms
- 🟢 Completing a multi-step qualification when the product doesn't exist
- 🟢 Spontaneous referral ("you should talk to my colleague who has this worse than me")
- 🟢 "When can I have it?" as the first reaction

## What does NOT count

- 🔴 "Looks interesting" / "cool idea"
- 🔴 Waitlist signup with no further action
- 🔴 Survey responses ("would you use this?" — stated future intent is noise)
- 🔴 Ad click-through with no post-click action
- 🔴 Compliments (see [`frameworks/the_mom_test.md`](../frameworks/the_mom_test.md) on why compliments are zero signal)

## How to run one — step by step

1. **State the hypothesis you're testing.** One sentence: *"Desperate customers in [narrow who] will [take a specific behavioral action] when shown [the concept]."*
2. **Pick the format** that gets the concept in front of the customer fastest (hours-to-days, not weeks).
3. **Define the behavioral threshold upfront.** What action, by how many people, counts as a pass? E.g., "3 of 10 qualified prospects book a paid pilot." Pre-register it so you can't move the goalposts.
4. **Get it in front of real customers in your narrow who.** Not friends. Not a general audience. The specific people from your discovery.
5. **Measure behavior, not words.** Did they do the thing, or did they just say nice things?
6. **Debrief.** Pass → proceed to implementation test or MVP. Fail → diagnose: is the concept wrong, the *who* wrong, or the messaging wrong? (Usually it's the *who* or the messaging before it's the concept — see [`frameworks/pmf.md`](../frameworks/pmf.md) on iterating the who.)

## Common failure modes

| Failure | Fix |
|---|---|
| Testing on friends / general audience | Test only on the narrow who |
| Concept test takes 3 weeks to build | You've drifted to an implementation test; simplify |
| Counting clicks/signups as signal | Demand behavioral commitment (pay, book, refer) |
| Asking "would you use this?" | Watch what they do; convert future questions to behavior |
| No pre-registered threshold | You'll rationalize whatever happens as success |
| Walking away on one weak test | Run multiple messages / formats before concluding |
| Pitching during a follow-me-home | Watch and ask; don't sell |

## Where this lives in the journey

- [Stage 03 — Problem-Solution Fit](../stages/03_problem_solution_fit.md) — concept testing candidate solution shapes
- [Stage 05 — MVP Build](../stages/05_mvp_build.md) — concept test precedes the build
- [`playbooks/validation_sequence.md`](validation_sequence.md) — the full concept → implementation → MVP sequence
- [`frameworks/the_mom_test.md`](../frameworks/the_mom_test.md) — the discipline that keeps the data honest

## Source

Synthesized from the Lean Startup MVP literature (Ries), the customer development methodology (Blank), and the validation sequence in [`frameworks/pmf.md`](../frameworks/pmf.md).
