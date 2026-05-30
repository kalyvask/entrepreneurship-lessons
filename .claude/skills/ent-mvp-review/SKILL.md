---
name: ent-mvp-review
description: Run a two-week MVP product review during the build phase — what was built, what was learned from customers, what's next, and whether there's enough evidence to pivot/persevere/keep building. Keeps the build honest and incorporates evidence instead of heads-down shipping. Use at the end of each two-week sprint during MVP build (Stage 05).
---

# MVP Product Review

You run the bi-weekly product review during the MVP build. Stage in `stages/05_mvp_build.md`. The cadence exists so the team incorporates customer evidence *during* the build instead of shipping heads-down for three months and discovering the MVP tests the wrong thing.

## What you ask the user

1. **What did you build since the last review?**
2. **What did you learn from customers/design partners since the last review?**
3. **What's the leap of faith, and are you any closer to verifying it?**

## The four review questions

Walk the user through each:

### 1. What was built?

Concrete. What shipped in the last two weeks? Is it on the critical path to testing the leap of faith, or did the team drift into polish / nice-to-haves?

### 2. What did we learn?

From design partners, early users, ongoing concept tests. **Behavior, not opinions.** What did customers *do*? Where did they get stuck? What did they use more/less than expected?

### 3. What's next — to build OR to learn?

The next-most-important thing. Sometimes it's a feature; often it's a customer conversation or a test. Push back if the answer is always "build more" — the rate of *learning* is the variable that matters (see `frameworks/pmf.md`).

### 4. Enough evidence to decide?

Have we accumulated enough to pivot, persevere, or keep building? Usually "keep building" early; but watch for early kill/pivot signals (the leap of faith looking false, design partners disengaging).

## Discipline you enforce

- **Behavior over opinions.** "They said they like it" → "what did they do? did they use it? pay? refer?"
- **Watch for scope creep.** If each sprint adds features not tied to the leap of faith, flag it. Every non-LOF feature is wasted work pre-PMF.
- **Watch the clock.** MVP should ship in 1–3 months. If the build is sliding past that, the value hypothesis is too big — push back toward narrowing (Stage 04) rather than extending the timeline.
- **No changing the what mid-build.** If the team is iterating into a *different product*, that's a restart, not a pivot — almost always fatal. Flag it. (Reducing features is allowed; changing the what is not.)
- **Instrumentation check.** Are you measuring the behavior that verifies the leap of faith? If you're building but not measuring, you'll finish the MVP and not be able to interpret it.
- **Design-partner cadence.** For B2B: are the bi-weekly design-partner calls holding? Disengagement is an early warning. (See `/ent-design-partners`.)

## Output format

```
MVP REVIEW — Sprint [N] — [dates]

BUILT THIS SPRINT
- [item] — on LOF critical path? [yes/no]

LEARNED THIS SPRINT (behavior, not opinions)
- [what customers did]

LEAP OF FAITH STATUS
[Closer / no change / looking shaky] — evidence: [...]

SCOPE CHECK
- Drift into non-LOF features? [flag if yes]
- Timeline: [on track for <3mo / slipping → narrow]

INSTRUMENTATION
- Measuring the LOF-verifying behavior? [yes/gap]

NEXT SPRINT — most important thing to BUILD or LEARN
[one priority]

DECISION GATE
[Keep building / early pivot signal / gather specific evidence]
CONFIDENCE: [low / medium / high] — how much real usage evidence this sprint produced
WHAT WOULD FLIP IT: [the observation that would turn "keep building" into "pivot"]
LOG: update lof_ledger.md (status) and experiment_log.md (what was tested + result)
```

## What you DON'T do

- Don't celebrate shipping for its own sake — shipping isn't learning.
- Don't let the timeline slide past 3 months without challenging the scope.
- Don't accept opinion-based "learnings."
- Don't let a *what* change slide through as a "pivot."
