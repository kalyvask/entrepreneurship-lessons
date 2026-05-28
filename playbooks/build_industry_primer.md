# Industry Primer Playbook

The industry primer is a 5–10 page document — internal, living, never published — that makes you **cocktail-party conversational** in your space. It is the foundation of primary research: you build it so that the limited time you get with experts is spent on what only humans can give you.

The primer is **not a deliverable.** It is a process. The thinking happens in the building.

## When to build it

- **RDI Phase 2** (after team alignment, before primary research starts) — [Stage 00](../stages/00_prepared_mind.md)
- When entering a new space you don't know well
- When pivoting to a new market or *who* — [Stage 07](../stages/07_pivot_or_persevere.md)

## Why bother

Without a primer, your interviews waste 20 of their 30 minutes on context. With a primer, every minute is spent on the questions only the human can answer.

The rule: **any question you can answer by Googling is not a good question to ask an expert during the limited time you have their attention.**

The primer harvests all the low-hanging fruit so your primary research can focus on what's actually hard to learn.

## The structure

A working template. Adapt to your space.

```
INDUSTRY PRIMER — [Space Name]
Last updated: [Date]
Owner: [Name]
Status: [Initial / Draft / Updated through 30 interviews / etc.]

1. OVERVIEW & MARKET HYPOTHESIS
   - What this space is
   - Why we're exploring it
   - Our working hypothesis about what's changing

2. STAKEHOLDERS AND RELATIONSHIPS
   2a. Stakeholder categories
       - For each: who they are, what they care about, how they're measured
   2b. Ecosystem map
       - Value chain
       - Workflows
       - Data flows
       - Regulatory influence

3. INDUSTRY DYNAMICS AND FORCES OF CHANGE
   3a. Macro forces (the change vectors)
       - Internal: regulation, labor, consolidation, power dynamics, standards
       - External: AI, IoT, demographics, capital costs, geopolitics
   3b. Headwinds and tailwinds
   3c. Capital, talent, attention flows
   3d. Historical inflections (when has this space transformed before?)

4. VOCABULARY AND INFORMATION SOURCES
   4a. Glossary of terms (insider vocabulary)
   4b. Watering holes (where industry conversation happens)
       - Trade publications
       - Conferences
       - Podcasts
       - Newsletters / Substacks
       - Industry-specific Reddit / Slack / Discord

5. STARTUPS, TECHNOLOGIES, AND EMERGING PLAYERS
   - Recent funding events
   - Notable spinouts
   - Adjacent technologies entering the space
   - Patents and IP signals

6. OPEN QUESTIONS AND EMERGING HYPOTHESES
   - What I don't yet know
   - What I'm testing
   - Where I expect to be wrong
```

## How to build it

### Step 1 — Scope sentence

Write the scope in one sentence:

*"We're exploring [space] because we believe [change is happening] is creating [opportunity for someone]."*

If you can't write this without it being either too broad ("food") or too narrow ("a CRM for vertical farm GMs in Brooklyn"), do RDI Phase 1 (team alignment) first.

### Step 2 — The landscape sweep

Spend 1–2 days on secondary research, in this order:

1. **Industry reports** — IBIS World, CB Insights, EBSCO, ProQuest for market size, segmentation, growth.
2. **Public companies in the space** — find the 3 most relevant; read their **earnings call transcripts** and 10-Ks. Free, rich, often surprising. Companies say things in earnings calls they'd never say to a startup.
3. **Player databases** — D&B Hoovers, Tracxn for incumbents; Pitchbook, Crunchbase for startups; recent funding events.
4. **Conversation venues** — trade pubs, industry newsletters, podcasts, conferences. Subscribe to 5–10 newsletters in the space immediately.
5. **Insider perspectives** — Tegus and AlphaSense for expert interview transcripts (paid). Google Scholar and patent databases (free) for technical / research-driven spaces.

If you have institutional access (university, employer) to paywalled industry reports or expert transcripts, lean into it while you have it.

### Step 3 — AI as accelerator

Use AI to compress the early reading. Specifically:

**Industry overview prompt:**
> *"Act as an industry analyst. Help me build a primer on [space]. I need:
> 1. A 1-paragraph overview of the space — what it is and what's happening
> 2. The 5–7 most important players and what makes each distinctive
> 3. The macro forces shaping the space over the last 2–3 years
> 4. The vocabulary — terms an outsider needs to know
> 5. The watering holes — where insider conversation happens
> 6. Specifically counterintuitive insights — don't repeat what's easily Googleable
> 7. Name what you're uncertain about
>
> Use specific names, numbers, and dates. Flag where you're inferring vs. citing. Output as Markdown."*

**Change vector identification:**
> *"What are the most important changes happening in [space] over the last 2 years? For each change, name:
> - What changed
> - Why it changed
> - Who's most affected
> - What new opportunities or constraints it creates
> - What 5 experts you'd talk to to validate this
> Output as a table."*

**Caveat:** AI is trained on broadly available content. It cannot give you the things behind paywalls, in expert transcripts, or in private conversations. Use it for the easy part; do the hard part yourself.

**Critical discipline:** the primer is for *you*. If you can defend the synthesis only by referring back to AI output, you haven't learned it. Read what the AI generated, then **write the primer in your own words.**

### Step 4 — The ecosystem map

A visual. Excalidraw, paper, Miro — any tool works.

- Boxes for each player type (incumbents, startups, customers, suppliers, regulators, etc.)
- Arrows for relationships (who pays who, who depends on who, who governs who)
- Labels for the friction points you've heard about

The first draft is messy. The second draft is clearer. Iterate until the structure of the space is visible at a glance.

### Step 5 — Identify the open questions

The last section of the primer. **The most important section.** Open questions are what your primary research will test.

Examples of good open questions:

- *"Mid-market operators say they can't afford enterprise software but pay $X/year on consultants. What's the path from consulting spend to software spend? When does it happen?"*
- *"Investors say the space is consolidating but operators say it's fragmenting. Who's right?"*
- *"Patents indicate research interest in X but no startups have entered. Why not?"*

A primer with good open questions sets up productive interviews. A primer with no open questions means you haven't synthesized — you've just collected.

## How to update it

The primer is **living.** Update it through Phase 3 of RDI (or through customer discovery in Stage 02).

After every 5–10 interviews:

1. **What did I add to the vocabulary?** New terms, new framings.
2. **What did I learn that I didn't expect?** Surprises go in the open-questions section if they generate new ones.
3. **What did I refine?** Existing hypotheses get sharpened or weakened by new data.
4. **What's a new stakeholder category I should add to the ecosystem map?**

## Common failure modes

| Failure | Fix |
|---|---|
| Treating it as a deliverable | The thinking is in the writing; the document is a side effect |
| Over-investing in production | Markdown / Notion is fine. Don't polish. |
| Stopping at the primer | The primer is prep. The learning is in the conversations. |
| AI-generated wall of text | Write in your own words; AI for ramp-up, not for the artifact |
| No open questions section | You haven't synthesized; you've just collected |
| Static (never updated) | Update at every 5-interview milestone |
| Generic | Specific names, numbers, dates throughout |

## Sharing the primer

The primer is **internal**. Don't publish it.

But: **drafts of frameworks, observations, or specific takes** can be published as you go. See [`frameworks/rdi.md`](../frameworks/rdi.md) on the value of public sharing during research.

## Where this lives in the journey

- [Stage 00 — Prepared Mind / RDI](../stages/00_prepared_mind.md) — primary use
- [Stage 02 — Customer Discovery](../stages/02_customer_discovery.md) — when entering a new segment
- [Stage 07 — Pivot or Persevere](../stages/07_pivot_or_persevere.md) — when pivoting to a new space
- [`templates/industry_primer.md`](../templates/industry_primer.md) — fill-in template

## Source

Stanford GSB STRAMGT 546 (RDI) "Building a Primer" methodology (Brady/Jordan); informed by Steve Blank's "Ten Steps to Map Any Industry" (2022).
