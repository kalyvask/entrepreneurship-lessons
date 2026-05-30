# Stage 01 — Insight and Idea Selection

> John Vrionis's distinction: ideas are everywhere and cheap; insights are rare, and they're the thing worth investing in.

The deliverable of this stage is a **falsifiable bet** built on a **non-consensus insight** about a **technological or market inflection**.

That's a lot of constraints. Each word is doing work.

- **Falsifiable** — you can write down what would prove it wrong.
- **Bet** — a specific commitment, not a wish list of possibilities.
- **Non-consensus** — informed people disagree with you (or haven't thought about it).
- **Insight** — a structured belief you can articulate, not a vibe.
- **Technological or market inflection** — something is *changing* such that what was impossible becomes possible (or what was possible becomes obsolete). Inflections create the demand for new companies. Without an inflection, you're competing on execution with incumbents — a losing position.

## Three kinds of "idea"

These get conflated and they shouldn't. Mixing them up is the most common reason early-stage teams spin.

| Type | What it is | What it's worth |
|---|---|---|
| **Wish** | "It would be cool if [X] existed" | Nothing. Wishes have no insight behind them. |
| **Idea** | "I think someone should build [X]" | Cheap. Lots of people had it. |
| **Insight** | "I believe [Y is changing], which means [X becomes possible/necessary], and I see this because [evidence]" | Investable. |

The point of [Stage 00](00_prepared_mind.md) was to *manufacture insight at industrial scale.* The point of this stage is to **convert insight into a specific bet** — and to be honest with yourself about which of the above you actually have.

## The shape of a great insight

An insight is a sentence. It has three parts.

> Because of [inflection / change happening in the world], it is now possible/necessary to [new capability], which existing players cannot pursue because [structural reason — RPV, incentives, channels, etc.].

Examples (paraphrased):

- *Wealthfront.* "Because investing fees have decoupled from cost of execution and software can now manage portfolios at the marginal cost of zero, it is now possible to deliver wealth management at a fraction of legacy private-banking pricing — which incumbent wealth managers cannot pursue because their cost structure is built around RIAs whose comp depends on the legacy fee model."
- *SpaceX.* "Because manufacturing precision and software-controlled landings have matured, reusable rockets are now possible — which existing launch providers cannot pursue because their entire R&D, supply chain, and pricing assume single-use boosters."
- *Anthropic.* "Because AI capabilities are advancing faster than safety understanding, there is now a meaningful market for an AI lab whose advantage is responsibility — which existing labs cannot pursue because their pricing and partnership models are built around speed-to-market."

You'll notice the structure: **a change vector** → **a new possibility** → **a structural reason incumbents are blind to it.** The third part is what gives you a moat in time. If the insight doesn't include the third part, you're racing against incumbents on the same wind, and incumbents have more resources.

## Where insights come from

You do not generate insights at a brainstorm. You **harvest** them from the research you did in Stage 00. They were probably there as early as the 10th interview but you didn't yet have the surrounding context to see them.

Practical method:

1. **Re-read your synthesis.** Cluster Analysis output from RDI. The labels of clusters that surprised you.
2. **Tension analysis.** Where do clusters contradict each other? Where do stakeholder perspectives diverge most? Those tensions are where insights live.
3. **Magic wand re-analysis.** Read back every "I wish I could…" line from interviews. Aggregate. Look for the wishes that the speaker has tried to solve themselves (the desperation signal — see [Stage 03](03_problem_solution_fit.md)).
4. **Change vector overlay.** For each candidate insight, ask: *what is changing right now that makes this possible/necessary now and not five years ago?* If the answer is "nothing in particular," it's not an insight — it's a perennial idea other people have already had.
5. **The "If you put it in your paper that…" test.** The PMF framework's filter: would informed people in this space disagree with this? If everyone in the space already agrees, it's consensus and you have no edge.

## The opportunity rubric

The opportunity rubric is the explicit filter you use to evaluate candidate insights. It exists because **you will fall in love with one and stop being objective**, and the rubric is your past self protecting your future self.

Recommended categories (see [`templates/opportunity_rubric.md`](../templates/opportunity_rubric.md) for a fill-in template):

**Insight & Inflection**
- Is there a clear, defensible change vector?
- Is the insight non-consensus among informed people?
- Why now? Why not 5 years ago, or 5 years from now?

**Market**
- Is the targetable wedge of customers narrow enough that you can manually reach 50 of them?
- Will it grow? (High-tide market, growing pool.)
- Can it become big enough? (Not your top concern pre-PMF, but a constraint.)

**Customer**
- Are these customers *desperate*, not just interested? (See [Stage 03](03_problem_solution_fit.md).)
- Can you reach them economically?
- Is the buyer the user, or are they different people? (Affects sales cycle profoundly.)

**Structural advantage**
- What can you do that incumbents structurally can't (RPV, channels, incentives)?
- Are there network effects, data effects, or learning effects that compound?
- Where is the moat *over time?* (Not just at launch.)

**Team fit**
- Do you have, or can you credibly recruit, the specific insight-and-execution skills this requires?
- Are you the right person to evangelize this for 10 years, not just to build the first version?
- Does it pass the "you'd be happy doing this even if it didn't work out" test?

**Deal-breakers**
- Regulatory risk you cannot tolerate
- Markets that require a specific identity you don't have
- Sales motions you've decided you won't run (e.g., 18-month enterprise cycles)
- Anything you wouldn't be proud of building

The rubric is **not a scoring system that picks for you.** It is a discipline that surfaces the trade-offs and forces you to be explicit about which you are accepting.

## The Marks 2x2

The course teaches a 2x2 from Howard Marks for thinking about how you should reason about your insight:

| | **Consensus is right** | **Consensus is wrong** |
|---|---|---|
| **You agree with consensus** | You're right but everyone else is too — no edge | You're wrong with the crowd |
| **You disagree with consensus** | You're wrong alone — costly | **You're right alone — the only place returns live** |

The bottom-right quadrant is the entrepreneur's job. The cost of operating there: most of the time *you're wrong alone* — humiliating, expensive, demoralizing. The reward: when you're right alone, the magnitude of the win is enormous because nobody else got there.

This is why **slugging percentage matters, not batting average.** You can fail nine times and succeed once and still win, *if* the magnitude of the success is enormous. The only way to be right consistently is to take very little risk — which means you're operating in the upper-left, where there's no edge.

## Sanity checks before you commit

Before you write the value hypothesis (Stage 04), have an honest conversation with yourself.

**The insight check**
- Can you articulate the insight in one sentence using the three-part shape (inflection → possibility → structural blindspot)?
- Would three different sophisticated people in the space disagree with you on at least one of the three parts?
- Do you have at least three pieces of evidence for the inflection that aren't "everyone says AI is changing things"?

**The motivation check**
- Why this problem? Why now? Why you?
- If this works, what does success look like in 10 years? Does that future excite you?
- What about this is going to be hard in a way you've already faced or can credibly face?

**The "lousy market" check**
- If this works mechanically but the market turns out to be smaller than you thought, is the consolation prize big enough? *(Rachleff: aim for a $100M revenue business — it takes the same amount of work as a $5M one.)*
- If this works mechanically but takes 5 years longer than you think, can you stay with it?

**The competition check**
- What are the closest existing solutions? Why do they not satisfy desperate customers?
- What would have to be true for an incumbent to pursue this? Why isn't it true? (Reference Christensen's RPV — Resources, Processes, Values.)

## Common failure modes in this stage

| Failure | Symptom | Diagnosis |
|---|---|---|
| Skipping straight to a solution | You wrote down "I'm building X" before doing the research | You have an idea, not an insight |
| Insight is consensus | Every podcast, every accelerator pitch deck mentions it | Race-to-market dynamic; no edge |
| Insight has no inflection | "There should be better X" without a "why now?" | Likely a perennial idea; incumbents will outspend you |
| Forcing the rubric | You bend criteria to make your favorite candidate pass | Take a week off. Re-run with a friend who's allowed to push back. |
| Too many candidates | You hold 6 opportunities loosely instead of 2–3 tightly | Prune. The teams that prune make faster progress than the teams that don't. |
| Premature pitching | You start pitching the insight before you can defend the third part of the sentence | Sales-driven thinking corrupts the research. Hold off. |

## Exit criteria — leaving this stage

You are ready for [Stage 02 — Customer discovery](02_customer_discovery.md) when:

1. You can write the insight in one sentence, using the three-part structural form.
2. Three sophisticated people in the space would meaningfully disagree with at least one element.
3. You have at least one specific candidate problem to test, with named hypotheses about *who* feels it most acutely.
4. You can credibly identify and reach 20–50 people who match the hypothesized customer profile.
5. The opportunity passes your rubric on all must-haves.
6. You are honest about what would prove the insight wrong.

If yes — go test it. Stage 02.
If no — Stage 00 isn't done. That's fine. The output of staying in Stage 00 longer than other people is *the edge that makes Stage 02 onward worth doing.*

## Required reading

- [`frameworks/pmf.md`](../frameworks/pmf.md) — the value hypothesis, insight, leap of faith
- [`frameworks/disruption_theory.md`](../frameworks/disruption_theory.md) — Christensen on why incumbents miss disruptive moves
- [`frameworks/ideation_templates.md`](../frameworks/ideation_templates.md) — systematic ways to expand the solution space around an insight (use after the research, not instead of it)
- [`frameworks/ten_star_product.md`](../frameworks/ten_star_product.md) — set the 10-star vision (is this worth a decade?) then narrow hard to the wedge
- [`templates/opportunity_rubric.md`](../templates/opportunity_rubric.md)
- [`templates/insight_statement.md`](../templates/insight_statement.md)

## Agent partner

`/ent-idea-coach` will walk you through harvesting insights from your research, structuring them into the three-part form, and pressure-testing each one against the rubric and the consensus filter. It will not let you ship an idea masquerading as an insight.
