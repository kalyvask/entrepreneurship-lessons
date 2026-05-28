# Pivot Decision Playbook

The pivot decision is the most important strategic decision a pre-PMF company makes. It is also the most commonly mishandled — most teams pivot too late, too small, or in the wrong direction.

This playbook is a structured process for making the call cleanly.

## When to consider a pivot

Trigger conditions:

- PMF self-check (see [`playbooks/pmf_assessment.md`](pmf_assessment.md)) scores 0–3 of 6
- You've shipped an MVP and 3–6 months of data shows weak retention, no organic growth, or no validated leap of faith
- Customers exist but they aren't desperate enough — they use the product, they like it, but they don't refer, they churn, they hedge on pricing
- Your gut says "we're pushing a boulder uphill" and the data doesn't disprove it

## The two-week pivot decision sprint

A structured timeline. Don't make this decision in a single meeting; the stakes are too high for emotional reactions to dominate.

### Day 1–3 — Diagnose the failure

Run the PMF self-check honestly. Identify which questions are RED.

Then map RED dimensions to pivot type:

```
Q1 + Q2 RED (wrong narrow who, leap of faith ambiguous)
   → Likely PIVOT THE WHO

Q1 OK but Q5 RED (right segment, Sean Ellis low)
   → Narrow further — pivot the WHO (deeper narrowing)

Q3 RED (retention asymptotes to zero)
   → Two paths:
     - One-time job → reconsider business model
     - Non-desperate base → narrow the WHO

Q4 RED (no organic growth)
   → Distribution issue → PIVOT THE HOW
   → OR desperation issue → PIVOT THE WHO

Multiple Qs RED including Q2 (LOF not verified across attempts)
   → Question whether the original INSIGHT is still right
   → RESTART might be needed (rare; high cost)
```

### Day 4–7 — Identify the over-performing slice

Scott Cook's "savor the surprise." Look in the data:

1. **Which customer cohort has 2–5× retention vs the average?**
2. **Which customer used the product the most? What's true about them that's NOT true about the average?**
3. **Which acquisition channel is converting and retaining? What's the buyer mindset there?**
4. **Which feature was used at 10× the rate of others?**
5. **Were there specific customers who were going to refer / pre-pay / sign LOI early, that you didn't follow up on?**

The over-performing slice tells you where PMF is, if there is PMF anywhere in your data. The pivot direction is **toward the slice**, not away from your failure.

If there's no over-performing slice — every cohort behaves similarly indifferently — the issue is upstream (your insight may be wrong, or the *what* doesn't address a real job). That points to restart territory or shutdown.

### Day 8–10 — Draft 2–3 candidate new value hypotheses

For each candidate, fill in the value hypothesis structure:

```
CANDIDATE PIVOT [N]
Type: [WHO pivot / HOW pivot / WHAT change (restart)]

NEW VALUE HYPOTHESIS
What: [Stays the same as before, OR specifically what changes]
Who:  [The narrow new audience — described specifically enough to find 50 of them]
How:  [Updated delivery / distribution / monetization]

LEAP OF FAITH
The one behavioral assumption that has to be true.

EVIDENCE
What in our existing data suggests this might work?
Where does the over-performing slice fit?

INVESTMENT NEEDED
- Engineering changes (be specific)
- Sales motion changes
- Time horizon to evidence

WHAT IT GIVES UP
- Which existing customers does this leave behind?
- Which past investment becomes wasted?
- What happens to current revenue / contracts?

WHAT WOULD FALSIFY IT
What evidence in the next 3 months would tell us this didn't work either?
```

Honest comparison across candidates. Don't pick the prettiest narrative — pick the one with the most evidence in current data.

### Day 11–13 — Stress-test with critics

A founders' feedback meeting (Rachleff's term — see [Stage 04](../stages/04_value_hypothesis.md)). Present the leading candidate to:

- A co-founder or trusted advisor who can disagree without consequences
- An existing customer (in the new *who* if possible)
- An investor (for unfiltered pushback, not approval)
- A skeptical industry expert

Their job is to argue the strongest case **against** the new hypothesis. Your job is to listen, not to defend.

Common failure modes that surface in feedback:
- The new *who* is still too broad
- The leap of faith is technical, not behavioral
- The strategy doesn't actually leverage existing assets
- The wishful element is still embedded ("but customers will of course do X")

### Day 14 — Decide

Three options:

**1. Pivot.** Commit to the new value hypothesis. Set:
- Timeframe (3–6 months)
- Specific evidence threshold ("5 customers in the new narrow *who* pre-paying within 60 days")
- Trigger for next decision ("if by month 3 we don't have 3+ customers behaving X way, we revisit")

**2. Persevere.** The data was misread. Or you have a slice of PMF you didn't recognize. Recommit to the original hypothesis with sharper focus on the over-performing slice.

**3. Restart.** The original insight was wrong, not just the *who*. Pivot the *what* — a different product entirely. Rare; high cost. Almost always failure waiting to happen.

**4. Shut down.** Sometimes the right answer. If you've tried 2 pivots without finding the desperate customer, and there's no over-performing slice in your data, the right move is to wind down and start something different.

## The communication

The pivot has communication consequences:

### Existing customers

Will the pivot leave them stranded?

- If yes: be honest. Offer to wind down their account at a discount. Don't ghost.
- If they fit the new *who* too: explain the focus change clearly.

### Investors

Pivots are normal but they need a story that holds together.

- The story should be the data, not the narrative.
- Walk them through the failure analysis, the over-performing slice, the new hypothesis, the timeline.
- They will push back. That's their job. Hear it.
- If they don't believe in the new hypothesis: take their concerns seriously, but they're not the customer. Their pushback is signal but not deciding.

### The team

Pivots are also human transitions:

- Some people joined for the old vision. Some won't make the new one. Have honest conversations.
- Engineering roadmap shifts. The product backlog from 6 months ago is now mostly irrelevant.
- Morale takes a hit on every pivot. Acknowledge it. Don't pretend nothing changed.

### Co-founders

Pivots are relationship tests. Do this **in writing**, not just verbally:

- Pivot memo signed by both/all founders
- Explicit agreement on the new hypothesis, timeline, threshold
- Explicit agreement on what happens if it doesn't work (next move)

See [`templates/pivot_memo.md`](../templates/pivot_memo.md).

## The death-pivot pattern (avoid)

A common failure: pivoting every 2–3 months without giving any single hypothesis time to play out.

Symptoms:
- Each pivot is "this time we figured it out"
- New decks every quarter
- The product changes substantially every month
- Engineering is constantly building "the new thing" rather than learning from "the current thing"

The fix: **commit to a single pivot for 3+ months minimum.** Test it cleanly. Either it works or it doesn't. If it doesn't, the next decision is restart or shutdown — not another pivot.

## Common failure modes

| Failure | What it looks like | Why it kills you |
|---|---|---|
| Adding features instead of pivoting | "If we add X, our lukewarm customers will convert" | Rachleff: "lunacy." Features don't make people desperate. |
| Restart instead of pivot | "This product doesn't work, let's build something else" | You waste the insight. The *who* was almost certainly the issue. |
| Death pivot | Pivoting every 2 months | Don't give any hypothesis time to play out |
| Late pivot | "One more quarter" repeated 4 times | Runway evaporates |
| Pretending to pivot | New deck, same hypothesis | Investors see a pivot; customers see nothing |
| Pivoting on one disappointed customer | One big lost pilot → "let's restart" | Outlier in small data |
| Pivoting on investor pressure | "Our VC thinks we should pivot" | Your VC isn't the customer |
| Skipping the founders' feedback | "We know what to do" | You're in love with the narrative |
| No written commitments | Verbal agreement only | Memory drifts; no accountability |

## A specific pattern: narrowing-as-pivot

The most common successful pivot is **further narrowing of the *who***, not a change in direction.

If your original *who* was "engineering managers at tech companies" and PMF is elusive, the pivot might be "engineering managers at 50–200 person SaaS companies who joined in the last 6 months."

This isn't a "real" pivot in the dramatic sense — but it's the move that most often works. Same product, same insight, much sharper *who*.

Wealthfront is the canonical example: started as "automated investing for tech workers," progressively narrowed to "engineers in consumer-focused tech companies about to go public, with under $1M in assets, who were reluctant DIY index investors." Same *what* the whole time.

If your pivot candidates all involve dramatic changes, ask: is there a narrower version of the *original* hypothesis that no one tested?

## Where this lives in the journey

- [Stage 07 — Pivot or Persevere](../stages/07_pivot_or_persevere.md) — the home of pivot decisions
- [`frameworks/rachleff_pmf.md`](../frameworks/rachleff_pmf.md) — iterating the who not the what
- [`templates/pivot_memo.md`](../templates/pivot_memo.md) — the written commitment

## Source

Rachleff's pivot discipline; Ries's pivot taxonomy; Blank's customer development; the Wealthfront and Broadcom case studies cited throughout.
