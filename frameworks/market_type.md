# Market Type (Steve Blank)

> Blank's rule: **market type changes everything.** The same product, sold into a different market type, needs a different sales process, a different burn rate, a different definition of success — and a different time to PMF.

Most founders pick a product and a customer and never consciously pick a **market type**. That omission is expensive. Blank's contribution in *The Four Steps to the Epiphany* is that the *type of market you are entering* — not the product — is the single biggest determinant of how you sell, how big the market is on day one, how you position, and how fast (or whether) product-market fit shows up. Run an existing-market playbook in a new market and you build demand-gen for a thing nobody is searching for. Run a new-market playbook in an existing market and you evangelize a category that already exists while a competitor out-executes you on the axis customers already care about.

This framework is upstream of positioning. You decide market type, and positioning, sizing, and the sales motion fall out of it.

## The four market types

| Type | What it is | Do customers exist? | Basis of competition | Example |
|---|---|---|---|---|
| **Existing market** | A defined market with known competitors and known customers | Yes — they already buy a solution | **Better / faster performance** on the axis customers already measure | A faster database; a better CRM |
| **Resegmented market** | An existing market sliced into a defensible sub-segment, either by **niche** (different value to a subset) or by **low cost** (good-enough, cheaper) | Yes, but underserved on your axis | **Different value** to a specific segment incumbents serve poorly | Southwest (low-cost air travel); a vertical SaaS for one industry |
| **New market** | A market that does not exist yet — you enable consumption that wasn't possible before | **No — customers don't exist yet** | **"Does anyone care?"** — latent need, not a feature race | The first tablet; Airbnb-style stranger lodging |
| **Clone market** | A proven model from another geography, localized | Yes, elsewhere | **Local knowledge** and adaptation | A regional clone of a working US model |

Most winning startups are **resegments**, not true new markets. Resegmenting is the entrepreneurial sweet spot: the demand is proven (customers already spend money on the job), but you serve a slice the incumbent structurally can't, which is exactly the "narrow who with a structural edge" the rest of this library pushes you toward.

## How market type changes everything

| Dimension | Existing market | Resegmented market | New market |
|---|---|---|---|
| **Market size day one** | Large, known — but you fight for share | Smaller, knowable — the slice you pick | ~Zero, unknowable — you create it |
| **The customer** | Already buying; comparison-shops | Buying, but unhappy on your axis | Doesn't know they're a customer yet |
| **Basis of competition** | Performance on the known axis | A different axis (niche value or price) | Education: does the need exist? |
| **Sales / positioning** | "Better/faster than [incumbent]" | "The [category] for [segment]" | "A new way to [job], because [inflection]" |
| **Biggest risk** | Incumbents outspend you | You picked a slice too small or not actually underserved | Adoption never comes; you run out of runway educating |
| **What PMF looks like** | Fast switching and head-to-head wins | Pull from the underserved slice | Slow, then sudden — latent desire converting to behaviour |
| **Time to PMF** | Fast (if you're genuinely better) | Medium | **Long** — budget for it |

## Choosing your market type

Walk the questions in order:

1. **Do customers already pay something to get this job done?**
   - No → you are likely in a **new market**. Your job is to prove latent demand exists, not to win a feature comparison.
   - Yes → continue.
2. **Are you better on the axis customers already measure, and can you stay ahead?**
   - Yes, with a structural edge → **existing market**. (Without a structural edge, head-on is a losing position — incumbents have more resources. See [`disruption_theory.md`](disruption_theory.md) on RPV.)
   - No → continue.
3. **Can you serve a specific underserved slice better, or deliver good-enough for far less?**
   - Niche value → **resegment (niche)**. Good-enough, cheaper → **resegment (low-cost)**. This is usually the answer.
4. **Is this a proven model elsewhere that doesn't exist in your geography?** → **clone**.

The choice is a hypothesis like any other in this library: write it down, and let discovery confirm or break it.

## When to create a new category (and when not to)

A new market usually means **creating a new category** — and that is a heavy, expensive commitment, not a positioning flourish.

- **Create a category only when** existing categories genuinely don't fit, the incumbent frame would cause customers to misjudge what you are, and the value is genuinely new. The signal: prospects keep asking "so it's like [X]?" and every analogy actively misleads.
- **Don't create a category when you can win as a resegment.** Category creation forces you to *educate the market* — the slowest, most capital-intensive thing a startup can do. If customers already understand the category and you can own a slice of it, do that instead.
- **How, if you must:** be ruthlessly clear on the value, name the problem in the customer's language, educate relentlessly, lead with storytelling over spec sheets, and build the surrounding ecosystem (partners, references, vocabulary). See [`crossing_the_chasm.md`](crossing_the_chasm.md) — a new category eventually faces the chasm like any other.

## Positioning follows from market type

Positioning is not a separate creative act; it is the output of your market-type choice. The one-line statement:

> For **[target customer]** who **[need / problem]**, **[product]** is a **[category]** that **[key benefit]**. Unlike **[primary alternative]**, we **[differentiator]**.

The `[category]` and `[primary alternative]` slots are *determined by market type*:

- **Existing market** → the category is known; the alternative is the incumbent; you differentiate on performance.
- **Resegment** → the category is known; the alternative is "the generic incumbent"; you differentiate by fit to the segment ("the X *for* [segment]").
- **New market** → there is no clean category or alternative; the comparison is "the status quo / doing nothing," and you differentiate on a newly-possible capability.

Fill it in with [`../templates/positioning_statement.md`](../templates/positioning_statement.md).

## The PMF connection

Market type changes the **timeline and the signal of product-market fit, not the bar.**

The bar is unchanged: desperate customers, behaviour over opinions, organic pull (see [`pmf.md`](pmf.md)). But *how that evidence appears depends on the market*. In an existing market, PMF shows up early and loud — fast switching, head-to-head wins, short sales cycles. In a **new market, desperation is latent**: customers can't search for what they can't name, adoption is slow then sudden, and an early Sean Ellis survey will under-read fit because the user base is tiny and still being educated.

The trap cuts both ways. Founders in a new market who expect existing-market speed declare failure too early and death-pivot a thing that was working on a longer clock. Founders who *use* "it's a new market, it takes time" as an excuse never confront the absence of desperation. The discipline: **adjust the timeline and read the market-appropriate signal — never lower the desperation bar.** When this tension bites, see [`conflicts.md`](conflicts.md).

## How this differs from adjacent frameworks

- **vs. Christensen's new-market disruption** ([`disruption_theory.md`](disruption_theory.md)): disruption is a *mechanism* by which an entrant displaces incumbents (from a low-end or non-consumption foothold). Market type is a *go-to-market decision* about which kind of market you are entering. A new-market disruption is often launched as a Blank "new market," but the frameworks answer different questions: disruption says *why incumbents won't follow*; market type says *how you sell and how to read success*.
- **vs. Crossing the Chasm** ([`crossing_the_chasm.md`](crossing_the_chasm.md)): Moore describes the adoption lifecycle *within* whichever market you've chosen. Market type is the prior choice; chasm dynamics play out afterward.
- **vs. Value Dimensions / JTBD** ([`value_dimensions.md`](value_dimensions.md)): those tell you *why a given customer pays*; market type tells you *what competitive world you're paying into*.

## Common failure modes

| Failure | Why it kills you |
|---|---|
| Running an existing-market feature war in what's really a new market | Nobody is searching; demand-gen spend lands on an empty market |
| Calling yourself a "new category" when you're a resegment | You pay category-education costs you never needed; a focused resegment beats you |
| New market, existing-market timeline | You expect fast pull, panic at slow adoption, and death-pivot something that was working |
| Existing market with no structural edge | You compete head-on on the incumbent's axis and get outspent |
| Sizing a new market with a TAM slide | The market doesn't exist yet — size the wedge and the adoption curve, not a top-down TAM |
| Never choosing a type | Your sales motion, pricing, and PMF expectations are incoherent because they assume three different markets at once |

## Where this lives in the journey

- [Stage 01 — Insight & Idea Selection](../stages/01_insight_and_idea.md) — which market type your bet implies is part of the bet
- [Stage 04 — The Value Hypothesis](../stages/04_value_hypothesis.md) — the *who* and the positioning follow from market type
- [`crossing_the_chasm.md`](crossing_the_chasm.md) — adoption dynamics within the market you chose
- [`disruption_theory.md`](disruption_theory.md) — the displacement mechanism, distinct from market type
- [`conflicts.md`](conflicts.md) — reading the PMF signal by market type
- [`../templates/positioning_statement.md`](../templates/positioning_statement.md) — the positioning one-liner this produces

## Source

Steve Blank's market-type framework, from *The Four Steps to the Epiphany* (2005) and *The Startup Owner's Manual* (Blank & Dorf, 2012). Synthesized with Geoffrey Moore's adoption work and the Lean Launchpad "Markets, Categories & Positioning" lecture (Stanford ENGR 245). Type: **synthesis** — ideas restated in this repo's words, consistent with `SOURCES.md`.
