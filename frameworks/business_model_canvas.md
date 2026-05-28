# Business Model Canvas (Osterwalder)

A single-page visualization of how a business creates, delivers, and captures value. Developed by Alexander Osterwalder; central tool of *Business Model Generation* (2010); core teaching device of Lean Launchpad methodology.

The canvas is not a strategy; it's a **structure for hypotheses**. Each block is a guess about how the business will work. The canvas's value is in forcing you to make those guesses explicit, then test them.

## The nine blocks

```
┌──────────────┬──────────────┬─────────────┬──────────────┬──────────────┐
│  KEY PARTNERS│  KEY         │   VALUE     │   CUSTOMER   │   CUSTOMER   │
│              │  ACTIVITIES  │ PROPOSITION │ RELATIONSHIPS│   SEGMENTS   │
│              ├──────────────┤             ├──────────────┤              │
│              │  KEY         │             │   CHANNELS   │              │
│              │  RESOURCES   │             │              │              │
├──────────────┴──────────────┴─────────────┴──────────────┴──────────────┤
│            COST STRUCTURE             │             REVENUE STREAMS     │
└───────────────────────────────────────┴─────────────────────────────────┘
```

### 1. Customer Segments
*Who* you're creating value for. Not demographics — specific customer groups with specific characteristics, jobs, and decision-making patterns.

Hypothesis to test: *we believe our value proposition matters most to [segment].*

### 2. Value Proposition
*What* you're offering that solves a problem or satisfies a need. The bundle of products and services that creates value for a segment.

Hypothesis: *we believe [segment] will choose us over alternatives because we deliver [specific value].*

### 3. Channels
*How* you reach the segment to deliver value — awareness, evaluation, purchase, delivery, after-sales support.

Hypothesis: *we believe [segment] discovers, evaluates, and buys through [specific channels].*

### 4. Customer Relationships
The kind of relationship you have with each segment — personal assistance, self-service, automated, communities, co-creation.

Hypothesis: *we believe [segment] needs/wants [specific relationship type] to use us.*

### 5. Revenue Streams
*How* the business makes money — usage fees, subscription, licensing, asset sale, brokerage, advertising.

Hypothesis: *we believe [segment] will pay [pricing structure] for [value].*

### 6. Key Resources
*What* assets are required — physical, financial, intellectual, human.

Hypothesis: *we believe we can acquire/build [resources] at scale.*

### 7. Key Activities
*What* the business must do to deliver the value proposition — production, problem solving, platform/network.

Hypothesis: *we believe [activities] are sufficient to deliver value.*

### 8. Key Partners
*Who* the business depends on outside its boundaries — suppliers, alliances, joint ventures.

Hypothesis: *we believe [partners] are required for the model to work, and they will work with us.*

### 9. Cost Structure
*How much* it costs to operate the business model — fixed and variable costs.

Hypothesis: *we believe cost structure looks like [specific breakdown] at scale.*

## How the canvas is used in Lean Launchpad

The Lean Launchpad methodology uses the BMC as the central organizing tool:

- **Week 1**: each team fills out their initial BMC. Every block is hypothesis at this point.
- **Each subsequent week**: teams go talk to ~10–15 customers/partners/suppliers and **test** the hypotheses in specific blocks. They mark blocks Green (validated), Yellow (need more evidence), or Red (disproved).
- **At every class**: teams present *how their canvas changed* — what they learned, what they pivoted, what's now Red.
- **By Week 10**: most teams have changed the canvas dramatically. The teams that haven't haven't done customer development.

The canvas is **never finished.** It is a working document for the search for product-market fit.

## How to use it without Lean Launchpad's structure

The BMC works as a personal discipline whenever you need to **structure thinking about a business model**:

1. **First draft** — fill in your hypotheses, fast. Use sticky notes (physical or digital) so you can move them.
2. **Identify the riskiest hypotheses** — for each block, ask: *if this turns out to be wrong, how badly does the model break?* The blocks most likely to break the business if wrong are the leap-of-faith candidates. Address them first.
3. **Plan tests for the riskiest** — for each high-risk hypothesis, design a cheap test (concept test, smoke test, conversation). What evidence would change your confidence?
4. **Color-code as you learn** — Green for validated, Yellow for partial, Red for disproved.
5. **Revisit weekly** — what changed?

## What the canvas is good at — and what it isn't

**The BMC is good for:**
- Forcing you to make hypotheses explicit
- Seeing the whole business model on one page
- Communicating the model to a team or advisor quickly
- Tracking what's been validated vs what remains hypothesis

**The BMC is not good for:**
- Generating insight (it organizes; it doesn't create)
- Replacing customer research (the canvas is filled in by the research)
- Surfacing the *leap of faith* (the canvas treats all blocks symmetrically; in reality, one or two assumptions are load-bearing for the whole business — those need separate attention)
- Identifying the *desperate customer* (segments are described too generically by default)

## Common failure modes

| Failure | What it looks like | Fix |
|---|---|---|
| Treating the canvas as the strategy | Spending weeks polishing a perfect-looking canvas | The canvas is hypotheses, not strategy. Go test it. |
| Vague Customer Segment | "Mid-market companies" | Narrow until you can name 10 specific people who match |
| Generic Value Proposition | "We help businesses save time" | Be specific about the job, the customer, and the alternative |
| Optimistic Revenue Streams | Pricing pulled from thin air | Triangulate from interviews with would-be customers |
| Forgetting Key Resources | Underestimating what you need | Be specific. What people? What capital? What IP? |
| Treating all blocks as equal-risk | Filling them all in evenly | One or two are load-bearing. Identify and prioritize them. |

## Sequence: BMC → value hypothesis → leap of faith

A working sequence:

1. **First pass at BMC.** Hypotheses across all 9 blocks. ~30 min.
2. **Identify the 1–3 riskiest hypotheses.** What would kill the business if wrong?
3. **Articulate the leap of faith.** Of the risky hypotheses, which is *the* one? (See [`frameworks/pmf.md`](pmf.md).)
4. **Write the value hypothesis** in the *what / who / how* shape. Use [Stage 04](../stages/04_value_hypothesis.md) discipline.
5. **Test the leap of faith first.** Design the cheapest possible concept test.
6. **Update the BMC** as you learn. Mark blocks Red/Yellow/Green.
7. **Iterate.**

The BMC organizes; the value hypothesis sharpens; the leap of faith focuses.

## Value Proposition Canvas (the companion)

Osterwalder later created a more focused canvas zooming into the *Customer Segments* and *Value Proposition* blocks. The Value Prop Canvas pairs:

**Customer Profile:**
- **Customer Jobs** — what they're trying to get done (JTBD)
- **Pains** — undesired outcomes, obstacles, risks
- **Gains** — desired outcomes, benefits, hopes

**Value Map:**
- **Products & Services** — what you offer
- **Pain Relievers** — how your offering reduces customer pains
- **Gain Creators** — how your offering produces customer gains

**Fit** is achieved when the Value Map maps cleanly to the Customer Profile.

See [`frameworks/value_prop_canvas.md`](value_prop_canvas.md) for the detail.

## Where this lives in the journey

- [Stage 01 — Insight and Idea](../stages/01_insight_and_idea.md) — first pass at the canvas
- [Stage 04 — Value Hypothesis](../stages/04_value_hypothesis.md) — tighten Value Prop + Customer Segments blocks
- [Stage 05 — MVP Build](../stages/05_mvp_build.md) — test the highest-risk blocks
- [Stage 06 — PMF Measurement](../stages/06_pmf_measurement.md) — confirm blocks are Green

## Source

*Business Model Generation* — Alexander Osterwalder and Yves Pigneur (2010). Companion: *Value Proposition Design* — Osterwalder et al. (2014). Both are central in the Lean Launchpad methodology and broadly in early-stage practice.
