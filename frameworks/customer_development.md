# Customer Development (Steve Blank)

> *"Get out of the building."* — Steve Blank

Steve Blank invented Customer Development. His 2005 book *The Four Steps to the Epiphany* is what Andy Rachleff calls *"the Old Testament"* — hard to read, highly influential, the book Eric Ries simplified into *The Lean Startup*.

The book that changed how engineers thought about startups. Before Blank, the dominant model was *Product Development* — engineers built what they thought customers wanted, shipped it, then "sold" the result. Blank's contribution: a *parallel* discipline, *Customer Development*, run by founders, dedicated to validating that what you're building has a desperate customer with a problem worth solving.

The framework's spine: **do not build an execution machine before you have validated value.**

## The four steps

Blank breaks the search for a scalable business into four sequential phases. Each phase has explicit deliverables and an exit gate. The team does not move to the next phase until the prior gate clears.

### Step 1 — Customer Discovery

Find out **who your customers are** and **whether they care** about the problem you have decided to solve.

The work:
- Articulate hypotheses about who would care, why, and what they'd pay
- Go talk to those people — *get out of the building*
- Listen for stories about their problems, not opinions about your idea
- Identify *earlyvangelists* — customers desperate enough to buy a half-finished solution
- Test the problem and the solution sketch

Exit gate: you can credibly claim that a specific group of customers has a specific problem severe enough that they'd pay for a solution.

This phase corresponds roughly to [Stage 00–02](../stages/00_prepared_mind.md) of the journey we describe.

### Step 2 — Customer Validation

Develop a **repeatable, scalable sales process** with paying customers.

The work:
- Build the smallest feature set that gets a customer to pay (the **Blank MVP**)
- Sell it. Actually sell it.
- Refine pricing, sales motion, channel, positioning
- Validate that a sales process can be repeated with new customers

Exit gate: you have closed enough deals with enough confidence in the pattern that the sales process is repeatable. You can predict how many calls / meetings / demos lead to how many closed deals. **The conditions for scale exist.**

This phase corresponds to [Stage 05–06](../stages/05_mvp_build.md) of the journey we describe.

### Step 3 — Customer Creation

Build end-user demand and funnel it into the sales channel.

The work:
- Start generating demand at scale
- Tune the engine of growth (paid, viral, sticky)
- Onboard customers across the chasm — from early adopters into early majority

This phase is the *growth hypothesis* phase in the Rachleff framework. It corresponds to the post-PMF execution phase.

### Step 4 — Company Building

Transition from a learning-and-discovery organization to an execution organization with formal departments.

The work:
- Build sales, marketing, engineering, finance, ops as functional departments
- Move from a discovery org to an execution org
- Hire managers and operators (different skill set than founders)
- Build process, OKRs, metrics

Most teams overlap this with Customer Creation. The Blank discipline insists they are different — and that premature company-building (formal departments, fancy titles, OKR cycles) before Customer Validation is one of the great Silicon Valley failure modes.

## The pedagogical move that matters

The order is **inverted from how most MBA classes teach business strategy.**

Most strategy education starts at *Step 4* — write the business plan, run the financial model, build the marketing plan, set up the org chart. That's company-building thinking. It's appropriate for a company that already has product-market fit and is scaling. It is **disastrous** for a pre-PMF startup.

Blank's insight: **founders' job in Steps 1–2 is not to build a company. It is to find out whether there is a company to build.** The activities, mindset, metrics, and team structure are completely different.

## Earlyvangelists

Blank's term for the early adopters who buy MVPs from unknown companies. The behavioral profile:

- They have a **burning problem** that they cannot wait for the mainstream solution.
- They **buy on proof of concept**, not on references.
- They **tolerate broken products** because they need *something*.
- They **advocate inside their organizations** — they become your insider champion.
- They are willing to **pay for unfinished work** — pilots, betas, alpha access.

The strongest enterprise signal that someone is an earlyvangelist: **they have tried to build the solution themselves.** They've hacked together something. Their engineering team has an internal tool. They've hired a consultant. They've already spent money on this problem.

That is the signature Rachleff codified later as *desperation* — see [`frameworks/rachleff_pmf.md`](rachleff_pmf.md).

## Customer development ≠ market research

Rachleff is sharp on this point — and it's worth repeating because it's the most common misunderstanding of Blank's work:

> *"Customer development is selling people what you have and learning from their reaction. Market research is asking people what they want. They are categorically different."*

Real customer development:
- You already have an insight and a hypothesis.
- You are **selling** what you have, not asking what to build.
- You are not trying to overcome objections; you are trying to find the root cause so you can pivot the *who*.

When Blank's book opens with chapters about market hypothesis, market research, and customer segments before the customer development chapters, that's a pedagogical concession to MBAs who lack technical insights — not Blank's actual belief about the highest-probability path.

## Two MVP definitions to hold in parallel

- **Blank MVP:** *"The smallest feature set that will get a customer to pay for it."* — Economic validation focus.
- **Ries MVP:** *"The minimum functionality required to prove your leap-of-faith assumptions critical to the success of your business."* — Learning focus.

Different emphasis. Both useful. Rachleff/Vrionis synthesis: *"A usable product that either allows you to prove your leap of faith or gets a customer to pay you."* The OR matters.

For a behavioral leap of faith, focus on usable. For a willingness-to-pay leap of faith, focus on paid. Pick the primary.

## Get out of the building

The most quoted line in startup methodology. Blank's first principle.

There are no answers inside the building. Discovery happens in the market. The team that spends 80% of its early time talking to customers, reaching out, debriefing, and iterating beats the team that spends 80% of its early time building.

A pre-PMF founder's calendar should look like:
- ~50% customer-facing time (interviews, demos, sales calls, follow-ups)
- ~20% synthesis and decision-making time
- ~30% product (and ONLY when there's a sharpened hypothesis to build to)

Founders who spend 80% of their time building before they have validated hypotheses produce well-engineered software for problems that aren't desperate.

## Customer development as a parallel process

Blank's diagram has Product Development on one track and Customer Development on a parallel track. Both run simultaneously. The Customer Development track validates that the right thing is being built; the Product Development track builds.

The two tracks talk to each other — they're not independent — but they have **different skills, different success measures, and different cadences.** Founders are usually the Customer Development team in early stages. They cannot delegate it. Engineers are usually the Product Development team. They should not be the people doing customer development (different skill set, different mindset).

A team that has only engineers, no one good at customer development, will tend to over-build and under-validate. A team that has only customer-development types, no engineers, won't ship. You need both, and you need them in conversation.

## The connection to Rachleff and Ries

Three thinkers, one framework. Differences:

- **Blank** — original. Process-heavy. Dense. Best for systematic thinkers who'll execute the four steps with discipline.
- **Ries** — accessible. Vocabulary-rich. Best for the broad audience and the loop-based mental model.
- **Rachleff** — sharpest. Vocabulary precision matters. Best for the discipline of differentiating *pivot* from *restart*, *MVP* from *concept test*, *need* from *desperation*.

All three are required reading. None alone is sufficient.

## Where this lives in the journey

- [Stage 00 — Prepared Mind](../stages/00_prepared_mind.md) — pre-customer-discovery
- [Stage 02 — Customer Discovery](../stages/02_customer_discovery.md) — Step 1
- [Stage 03 — Problem-Solution Fit](../stages/03_problem_solution_fit.md) — end of Step 1
- [Stage 04 — Value Hypothesis](../stages/04_value_hypothesis.md) — explicit hypothesis articulation (pre Step 2)
- [Stage 05–06 — MVP Build / PMF Measurement](../stages/05_mvp_build.md) — Step 2 (Customer Validation)
- (Post-PMF) — Step 3 (Customer Creation) and Step 4 (Company Building)

## Source

*The Four Steps to the Epiphany* — Steve Blank (2005). Substantially expanded in *The Startup Owner's Manual* (Blank/Dorf, 2012). Blank's blog at steveblank.com has continued the work — including "Ten Steps to Map Any Industry" (2022) which is referenced in [`frameworks/rdi.md`](rdi.md) as a complementary tool for ecosystem mapping.
