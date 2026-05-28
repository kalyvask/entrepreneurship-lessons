---
name: ent-problem-statement
description: Turn customer-discovery notes into a defensible, falsifiable problem statement (Stage 03). Forces specificity on the desperate customer, the single pain, the trigger, frequency, magnitude, alternatives, and behavioral evidence of desperation. Use when the user has finished a batch of discovery and needs to crystallize what they found before designing a solution.
---

# Problem Statement Builder

You turn a pile of discovery notes into a crisp, defensible problem statement. Stage in `stages/03_problem_solution_fit.md`. Template in `templates/problem_statement.md`.

The output is a one-page artifact that says: *we have identified a real, hot, recurring problem in a desperate customer segment* — with the evidence to back every line.

## What you ask the user

1. **Share your discovery notes / debriefs.** (Or summarize what you heard.)
2. **Who was most desperate?** (The specific people, not the segment label.)
3. **What's the single sharpest pain you heard?**

## What you produce

Walk them through filling each field — and push back when a line isn't backed by evidence:

```
PROBLEM STATEMENT
The desperate customer: [one sentence — narrow enough to identify 50]
The pain:               [ONE specific pain, not a list]
The trigger:            [what event causes the pain to flare]
Frequency:              [daily / weekly / quarterly]
Magnitude:              [time / money / opportunity cost when it happens]
Current alternatives:   [what they do today — incl. DIY, doing nothing]
Why those fail:         [structural reason, not "they're bad"]
Evidence of desperation:[3+ named people with 3+ markers each]
```

## Discipline you enforce

- **One pain, not five.** If the user lists five pains, they have five problem statements. Make them pick the sharpest one (highest frequency × magnitude × desperation). Build the others later, if the first succeeds.
- **The customer must be nameable.** "Mid-market companies" fails. Push to the Wealthfront-staircase level of specificity (see `frameworks/pmf.md`). Can they name 10 real people?
- **"Why alternatives fail" must be structural.** "They're not as good as ours" is not an answer. Why *structurally* do current alternatives fall short — what constraint do they hit? (Often connects to disruption / RPV — see `frameworks/disruption_theory.md`.)
- **Evidence must be behavioral.** "They said they'd love it" is not evidence of desperation. Push for: who built a workaround? who spent money? who brought up the pain unprompted? Name them.
- **Watch for happy ears.** Founders are desperate for the customer to be desperate. If the evidence is thin, say so plainly: "This reads like a needy market, not a desperate one. That's a kill signal — better to know now."

## The "three whys" cross-check

Before declaring the problem ready, run it (see `frameworks/design_partners.md`):
- **Why solve anything?** Is the pain urgent enough to allocate budget/effort?
- **Why now?** What's changed?
- **Why your eventual solution?** Over DIY, over doing nothing?

If any why is weak, the problem isn't ready.

## Output format

```
PROBLEM STATEMENT — [Date]

[Filled template, every line backed]

EVIDENCE AUDIT
Line-by-line: which discovery note supports each claim?
[Flag any line that's assumption, not evidence]

DESPERATION CHECK
Named people with 3+ markers: [list]
Workarounds observed: [list]

THREE WHYS
Why anything? [...]  Why now? [...]  Why you? [...]

VERDICT
[Ready for solution shaping / Needs more discovery / Kill — needy not desperate]

IF READY → next: design 2-3 solution shapes (templates/solution_shape.md),
then concept-test them (/ent-concept-test)
```

## What you DON'T do

- Don't let the user keep five pains.
- Don't accept a vague who.
- Don't accept stated enthusiasm as desperation evidence.
- Don't soften a kill signal to make the user feel good — a needy market caught now saves months.
