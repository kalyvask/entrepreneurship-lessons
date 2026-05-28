# The Founders' Feedback Meeting

A ritual for pressure-testing your value hypothesis before you commit to building. The panel's job is to **criticize, not to approve.** Your job is to **listen, not to defend.** The team owns the decision at the end — the panel does not vote.

This is the single most useful hour you can spend between writing a value hypothesis (Stage 04) and building an MVP (Stage 05). It surfaces the fatal flaw while it's still cheap to fix.

## Why it works

Founders fall in love with their value hypothesis. Love makes you blind to the flaw that a stranger would spot in thirty seconds. The founders' feedback meeting borrows the discipline of academic defense and venture pitch: you put the hypothesis in front of people whose explicit job is to attack it, and you train yourself to absorb the attack without defending.

The discipline of *not defending* is the hard part. Every instinct says to explain why the criticism doesn't apply. Resist it. The criticism is data. You're not there to win the room; you're there to find out where the hypothesis is weak.

## Who to invite

A panel of 4–6, deliberately chosen to attack from different angles:

- **A skeptic** — someone constitutionally inclined to poke holes. A blunt former colleague, an investor who passed, a curmudgeon you respect.
- **A customer** — ideally someone in the narrow *who*. They'll tell you whether the value proposition lands.
- **A domain expert** — someone who knows the space cold and can spot the structural reason it won't work.
- **An operator** — someone who's built something and knows where the execution lands mines.
- **A peer founder** — someone in the trenches who'll ask the questions an investor would.

Avoid: people who love you and want you to feel good. They're the worst panel because their encouragement feels like validation and isn't.

## How to run it

### Before (you prepare)

- Write the value hypothesis on one page: *what / who / how / leap of faith.* (See [`templates/value_hypothesis.md`](../templates/value_hypothesis.md).)
- Send it to the panel in advance. No surprise pitches.
- Prepare to present in **5 minutes max.** If you can't, the hypothesis isn't sharp enough.

### During (90 minutes)

1. **Present (5 min).** The value hypothesis, the leap of faith, the evidence you have so far. No slides-as-theater — just the substance.
2. **Panel attacks (60 min).** Their job: argue why this fails. Your job: ask clarifying questions, take notes, *do not defend.* When you feel the urge to explain why they're wrong, write the criticism down instead.
3. **Open probing (20 min).** Now you can engage — but in the spirit of stress-testing, not winning. "If that's true, what would I need to see to believe the hypothesis still holds?"
4. **Close (5 min).** Thank them. You decide later, not in the room.

### After (you decide)

The team owns the decision. The panel informed it; they don't make it. Options:

- **Proceed** — the hypothesis survived; build the MVP.
- **Sharpen** — a specific element (usually the *who*) needs narrowing; revise and re-test.
- **Pivot** — the criticism revealed the hypothesis is aimed at the wrong customer; go back to Stage 02.
- **Kill** — the leap of faith doesn't hold and there's no version that does; better to know now.

## The questions a good panel asks

Use this as a self-check even if you can't assemble a panel. Run your hypothesis against these:

**On the insight**
- Is this actually non-consensus, or does everyone in the space already believe it?
- What's the inflection? Why now and not five years ago?
- Why can't an incumbent do this tomorrow? (What's the structural blindspot?)

**On the who**
- Can you name 10 real people who match this *who*?
- Is it narrow enough to manually reach 50 of them?
- Are they desperate (4 markers) or just interested?

**On the what**
- Is it specific enough to build to?
- What's NOT in v1? (If they can't answer, it's not scoped.)

**On the leap of faith**
- Is it one behavioral assumption, or five baked together?
- What experiment tests it most directly?
- What would prove it false?

**On the economics**
- Does the back-of-envelope work? (LTV/CAC > 3, payback < 24 mo.)
- Is there a psychological value dimension, or is this a commodity? (See [`frameworks/value_dimensions.md`](../frameworks/value_dimensions.md).)

**The killer question**
- "It's two years from now and this failed. What happened?" (Pre-mortem — surfaces the failure mode the founder is suppressing.)

## Common failure modes

| Failure | Why it kills the value of the meeting |
|---|---|
| Inviting only supporters | Encouragement feels like validation; you learn nothing |
| Defending instead of listening | You spend the hour winning the room instead of finding the flaw |
| Treating the panel's opinion as the decision | They inform; you decide. Don't outsource conviction. |
| No customer on the panel | You miss whether the value proposition actually lands |
| Presenting for 20 minutes | If you can't present in 5, the hypothesis isn't sharp |
| Skipping the pre-mortem | The founder's suppressed fear is usually the real risk |
| Doing it after you've built | The whole point is to do it *before* the expensive build |

## Where this lives in the journey

- [Stage 04 — Value Hypothesis](../stages/04_value_hypothesis.md) — run this before committing to build
- [Stage 07 — Pivot or Persevere](../stages/07_pivot_or_persevere.md) — run it again before committing to a pivot
- [`templates/value_hypothesis.md`](../templates/value_hypothesis.md) — the one-pager you present
- The `/ent-red-team` skill simulates a panel when you can't assemble one

## Source

The founders' feedback meeting is a ritual in the PMF framework. The pre-mortem technique is from Gary Klein (popularized by Kahneman). The "listen, don't defend" discipline echoes Annie Duke's *Thinking in Bets* on separating decision quality from ego.
