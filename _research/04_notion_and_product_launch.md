# Notion (AI Across the Company Lifecycle + Troubleshooting Guide) + Product Launch Cheatsheet

## Notion Page 1: AI Across the Company Lifecycle

**Subtitle:** From Inspiration to Operation: Advanced Prompting for Every Stage
**Source:** `https://app.notion.com/p/AI-Across-the-Company-Lifecycle-...`

### Session Overview

How to leverage AI across the entire business lifecycle: discovery → building → operating. Advanced prompting techniques that separate superficial AI use from transformative leverage. When (and when not) to use AI tools in business contexts. Real-world workflows using a vertical farming startup example.

### The Tool Stack (a current AI operating system for entrepreneurs)

**Core LLMs**
- Claude (Anthropic) — Deep analytical work, long documents, complex reasoning, coding
- ChatGPT (OpenAI) — Broad tasks, coding, rapid iteration
- Gemini (Google) — Multimodal tasks, Google workspace integration

**Productivity & Analysis**
- Notion — Knowledge management, documentation
- Read.ai — Meeting transcription and synthesis
- Gamma — AI-powered presentation design
- Howie.ai — Scheduling

**Development & Prototyping**
- Cursor — AI-powered code editor
- Claude-code — Command-line agentic coding
- Replit — Quick prototyping and deployment
- Gumloop — No-code automation workflows

**Visual & Data**
- Excalidraw — Diagrams and visual thinking
- vlm.run — Vision language model experiments

### AI Risks & Best Practices

**The Slop Problem.** AI will confidently hallucinate. Always verify: citations that don't exist, plausible but wrong facts (especially in niche domains), outdated information (knowledge cutoffs), logical-sounding nonsense.

**Verification Strategies:**
- Triangulation — Ask multiple AI systems the same question; compare answers
- Source checking — When AI cites something, find the original
- Domain expert review — Have a human spot-check
- Consistency testing — Ask the same question different ways

**Human-in-the-Loop.**
- AI Should Decide: formatting and structure, first drafts, routine analysis patterns, summarization
- Humans Must Decide: strategic direction, anything involving people's livelihoods, final approval on external communications, ethical gray areas

**Ethical Considerations:** disclosure (be transparent when AI generated), bias awareness, privacy (don't put confidential info into public AI), attribution.

### State of AI for Business (2025)

**Why Now Is Different**
- 2022–2023: ChatGPT Moment — consumer AI mainstream
- 2024: Capability Explosion — reasoning, multimodal, long context, agents
- 2025: Inflection Point — AI-native companies emerging, MBA skillset includes prompt engineering

**What's Actually Possible Now**
- Research & Analysis: synthesize 100+ interviews in minutes; generate market maps; identify patterns
- Content & Communication: draft investor decks, PRDs, memos; personalized outreach at scale
- Prototyping & Building: generate working code; design interfaces; build MVPs in hours
- Operations: automate analyses; monitor markets; generate executive summaries

**What AI Still Can't Do:** make high-stakes decisions; understand unique context without prompting; replace domain expertise; build relationships and trust.

### The VerticalGrow Example

**Opportunity:** Mid-market vertical farms (10K–100K sq ft) stuck on Excel + paper logs. Can't scale without scaling headcount. 10–20% waste rates.

**Solution:** GrowthOS — integrated farm management platform.

**Journey:** Discovery (RDI) → Building (PRD, PRFAQ, deck) → Operating (competitive intel, market monitoring).

### Part 1: Discovery (RDI Phase 1–3)

**Workflow 1: Market Exploration → Shortlist → Validation**

Good prompt anatomy:
- Specificity ("CEA" not "agriculture"; "leafy greens" not "food")
- Structured output requested
- Time-bound focus ("last 2 years")
- Pushes beyond obvious
- Meta-instruction ("What can't you answer?")
- Output format ("Clear headers")

Tool choice table:
| Goal | Tool | Why |
|------|------|-----|
| Initial broad research | Claude or ChatGPT | Good for synthesis |
| Finding recent news/data | Web Search, Perplexity | Accesses current info |
| Validating claims | Google Scholar, industry reports | AI might hallucinate stats |
| Mapping stakeholders | Claude + Excalidraw | Generate framework, visualize manually |

**Workflow 2: Building Your Industry Primer**

Create a 5–10 page document that makes you "cocktail party conversational." Use Deep Research mode. Prompt principles:
- Role-setting ("Act as industry analyst")
- Explicit structure
- Meta-instructions ("Name names," "flag uncertainty," "state assumptions")
- Prioritization ("counterintuitive over easily Googleable")
- Practical framing ("operator knowledge not investor narratives")
- Acknowledge limits

Don'ts: treat as gospel truth; stop here (primer is prep for primary research); share AI content externally without heavy editing.
Dos: use to build interview target list; reference for interview questions; update as you learn; treat as living document.

**Workflow 3: Stakeholder Mapping & Interview Target List**

Identify 50–100 specific people across the ecosystem. Segmentation by stakeholder type. Requests both archetypes (personas) and specific targets. Includes sourcing strategy.

**Workflow 4: Interview Guide Creation**

Structured-but-flexible guides for each persona. Specific persona context, explicit time structure, outcome-oriented, requests questions AND follow-up probes, tone guidance ("conversational not corporate").

**Workflow 5: Post-Interview Synthesis**

Step 1: Transcribe with Read.ai (automated).
Step 2: First-pass synthesis — comprehensive structure, explicit request for quotes (prevents paraphrasing loss), emotional signals, hypothesis testing, future-oriented.
Step 3: Cross-Interview Pattern Recognition after 5–10 interviews — looks across multiple data points, structured along multiple dimensions, tests for segmentation, drives toward hypotheses.

**Workflow 6: From Insights to Opportunities**

Turn patterns into testable business opportunities. Grounds AI in actual research (attached synthesis), forces evidence-based reasoning, structured evaluation framework, incorporates personal rubric, requests both bull and bear cases.

### Part 2: Building — From Opportunity to Business

**Workflow 7: Creating a PRD**

Section-by-section: Overview & ICP (template-driven, grounds in research, differentiated buyer-vs-user value props); User Stories; Discovery Strategy; Competitive Landscape; GTM & Sales; Full PRD Assembly.

**Workflow 8: PR/FAQ — The Backwards Business Plan**

Amazon's framework. Forces clarity on customer value and addresses hard questions upfront. Future-backward thinking, customer quote requirement, FAQ addressing hard questions (not just happy path), self-correcting instruction ("if vague, ask for detail"), journalist-readable test.

**Workflow 9: Investor Pitch Deck**

Two-step: Use Claude to structure content; use Gamma to design visuals. Explicit structure (proven seed deck flow), takeaway-driven slide titles, visual guidance, narrative arc question, grounding in actual traction.

**Workflow 10: Financial Models**

Trust AI on structure, not calculations. Bottom-up revenue model and unit economics. Grounded in real data, multiple views (revenue, unit econ, P&L), sensitivity analysis, hiring linked to milestones.

### Part 3: Operating — Running the Business

- **Workflow 11: Competitive Intelligence** — Automated monitoring + weekly synthesis prompt.
- **Workflow 12: Investment Opportunities** — Evaluate competitors, acquisition targets, fundraising scenarios. Bear case explicit.
- **Workflow 13: Meeting Synthesis & Action Items** — Read.ai auto-transcribes; Claude synthesizes.

### The 8 Meta-Lessons of Advanced Prompting

1. **Context is King** — More context = less guessing = less generic output.
2. **Structure Your Requests** — Clear structure = usable output.
3. **Role-Setting Changes Quality** — Primes the model for perspective and expertise.
4. **Iterative Refinement > Perfect First Try** — AI is collaborator, not one-shot oracle.
5. **Chain of Thought for Complex Tasks** — Breaking into steps improves quality.
6. **Ground in Real Data** — Attaching real data prevents hallucination.
7. **Meta-Instructions Guide Quality** — "If uncertain, say so," "state assumptions," "stop if vague."
8. **Explicit Output Format** — Copy-paste ready content.

### Common Anti-Patterns

1. The Vague, Open-Ended Question
2. Asking AI to Predict the Future
3. Treating Output as Final
4. Over-Relying Without Verification
5. Using AI for What It Can't Do (proprietary data, specific future events, high-stakes decisions, domain expertise)

### Closing line

> "AI won't replace you. But someone using AI effectively might."

---

## Notion Page 2: Troubleshooting Guide — When Prompts Don't Work

### Problem 1: Generic, Useless Output

**Symptom:** Sounds good but applies to anything — buzzwords, platitudes.
**Fix:** Add context, attach data, specific constraints, structured output, ask for evidence.

### Problem 2: Hallucinated Facts/Citations

**Symptom:** Confidently states wrong facts or cites sources that don't exist.
**Fixes:**
- Demand source URLs
- Use Web Search Tools (Perplexity, Claude with web search)
- Triangulation
**Red flags:** overly specific stats without context, perfect round numbers, citations to "recent studies" without dates, sources that sound real but vague.

### Problem 3: AI Keeps Misunderstanding What You Want

**Fix:** Add context layers, provide examples, use contrast (what good looks like vs. what bad looks like).

### Problem 4: Output Is Too Long/Short

**Fix:** Specify length explicitly, specify format, iterate.

### Problem 5: AI Ignores Your Instructions

**Symptom:** "Don't use buzzwords" → output still has buzzwords.
**Fixes:** Use positive instructions (instead of "don't do X" say "do Y"), put critical instructions first, use examples, add checkpoints.

### Problem 6: Inconsistent Quality Across Sections

**Fix:** Generate section by section, review, then continue. Specify quality bars per section.

### Problem 7: Output Isn't Actionable

**Fix:** Explicitly request action items, request decision framework.

### Problem 8: Can't Get AI to Be Critical/Skeptical

**Fix:** Explicitly request critique, assign adversarial role, request red team analysis.

### Problem 9: AI Won't Give You a Straight Answer

**Fix:** Force a choice, provide decision framework.

### Problem 10: Prompt Works Once, Fails When Reused

**Fix:** Make context explicit every time, template your prompts, version your prompts.

### Quick Diagnostic Checklist

When a prompt isn't working:
1. Did I provide specific context? (not "farms" but "10–50K sq ft leafy greens farms")
2. Did I structure the output request?
3. Did I include examples of what I want?
4. Did I attach relevant data/documents?
5. Did I specify length/format explicitly?
6. Did I put critical instructions first?
7. Did I request actionable outputs?
8. Did I ask AI to self-check quality?
9. Am I trying to do too much in one prompt?
10. Did I verify facts/citations aren't hallucinated?

### The Nuclear Option: Start Over

When to start fresh: iterated 5+ times with no improvement; AI keeps misunderstanding; quality degrading; you're fighting the AI's defaults.

---

## Product Launch Cheatsheet (Stanford MKTG 535)

### The Two Master Questions

- **Q1: Is there a market?** TAM/SAM/SOM, demand signals, growth, competitive intensity, WTP.
- **Q2: Can we make money?** Unit economics, pricing power, margins, path to profitability.
- **Opportunity = Market Need + Underserved by Competition + Company Can Do It**
- Every case answer must address both. A large market with no viable unit economics is a trap. Sometimes doing nothing is something.

### The 3 Value Dimensions (F / E / P)

- **Functional:** Does it work? Solves the problem? Table stakes.
- **Economic:** Saves money or time? Quantifiable ROI. Rational driver.
- **Psychological:** Status, identity, confidence, belonging.

Psychological value drives highest WTP and is hardest to replicate. Different segments derive different sources of value. Classify every benefit as F, E, or P. **If there's no P, the product is vulnerable to commoditization.**

### Customer Problem Awareness

Customers must know they have a problem before they'll buy a solution. Bill Joy: *"My biggest mistake was designing solutions for problems people didn't yet know they had."* If the problem is latent/invisible, your first job is education, not selling.

**Watch what customers DO, not what they SAY.** Stated preferences are unreliable — observed behavior in an MVP/pilot is the only credible demand signal. Interviews generate hypotheses, not validation.

### 8 Product Principles

| # | Principle | Key Insight |
|---|-----------|------------|
| 1 | Product for everyone = product for no one | Narrow beachhead first |
| 2 | "Face product" is most profitable | Psych value > functional specs |
| 3 | Don't listen — watch what they do | Behavior > stated preferences |
| 4 | If users can't categorize you, you've lost | Positioning clarity = prerequisite for adoption |
| 5 | Best products solve must-have problems | Painkillers not vitamins |
| 6 | Value = Functional + Economic + Psych | Emotional value = highest WTP |
| 7 | It all starts with the customer | Specific user + specific problem |
| 8 | Two questions: Market? Profitable? | All other analysis is secondary |

### 3C / 4C Analysis

| Dim | Key Questions | Quantify |
|---|---|---|
| Customer | Who buys? Why? JTBD? Segments? Switching costs? | TAM/SAM/SOM, WTP, CAC, LTV |
| Company | Assets/capabilities? RPV fit? Cost structure? | Burn rate, runway, margins |
| Compet. | Direct & indirect? Share? Positioning? | Share %, pricing, moats |
| Context | Macro trends? Regulatory? Tech shifts? Timing? | CAGR, regulatory timeline |

### Disruption Theory (Christensen)

- **Sustaining:** Better products for existing customers on existing trajectories. Incumbents almost always win.
- **Disruptive:** Simpler, cheaper, more convenient. Targets nonconsumers or overserved low-end. Entrants win.

| Type | Mechanism | Example |
|---|---|---|
| New-Market | Targets nonconsumers; new value network | Sony transistor radio, iPod |
| Low-End | Overserved customers; good-enough + cheaper | Minimills, discount retail |

**Litmus Test:** 1) Nonconsumers or overserved? 2) Simpler/cheaper/more convenient? 3) Incumbents have asymmetric motivation to ignore? 4) Viable upmarket path?

### Why Great Companies Fail (5 Root Causes)

1. **Resource Dependence** — Customers control the company; disruptive products get killed in resource allocation.
2. **RPV Mismatch** — Org processes + values optimized for sustaining business; org actively rejects disruptive opps.
3. **Upmarket Migration** — Higher margins pull company upmarket; cost structures rise.
4. **Performance Oversupply** — Tech improves faster than demand → basis of competition shifts.
5. **Bad Money** — Pressure for fast, large-scale revenue forces sustaining strategies.

### Functional Fixedness + Ideation

**Functional Fixedness:** Cognitive bias where people see objects/products only in their current form. We take things "as they are" and can't imagine alternatives. The #1 barrier to product innovation.

**"Thinking Inside the Box"** — Product-focused. Function follows form. Process: Diverge → Converge. Don't evaluate during diverge.

| Template | Method | Example |
|---|---|---|
| Subtraction | Remove an essential component | iCloud removed local storage |
| Task Unification | Assign new task to existing component | reCAPTCHA: security + digitize books |
| Division | Separate: Physical, Functional, or Preserving | Foam puzzle tiles (physical) |
| Multiplication | Copy a component but change it slightly | Multi-blade razors |
| Attribute Dependency | Create new dependency between 2 attributes | Transition lenses (light→tint) |

### JTBD + RPV + Strategy

- **JTBD:** Customers hire products for a job. Segment by circumstance, not demographics. Three dimensions: Functional, Emotional, Social. Ask: "What are they firing?"
- **RPV:** Resources = has. Processes = does. Values = prioritizes. Org's capabilities DEFINE its disabilities. Sustaining → mainstream org. Disruptive → autonomous unit.
- **Strategy:** Deliberate = top-down, analytical (sustaining). Emergent = bubbles up (disruptive). Use emergent until strategy crystallizes.
- **Basis of Competition:** Functionality → Reliability → Convenience → Price. Each shift = disruptive window. Interdependent architecture when not good enough; Modular when more than good enough.

### Discovery-Driven Planning

Assume forecasts are wrong. Reverse-engineer: required profit → needed revenue at what margins → list assumptions ranked by uncertainty → test critical ones first, cheaply → kill/pivot early. **Opposite of traditional planning: start with what needs to be TRUE, then test it.**

### Key Formulas

```
LTV = (ARPU × Gross Margin%) / Churn Rate
LTV:CAC > 3:1 = healthy        Payback < 12mo = good
Contribution Margin = Price − Variable Cost/Unit
Break-Even Vol = Fixed Costs / Contribution Margin
Gross Margin% = (Rev − COGS) / Rev
CAGR = (End/Start)^(1/n) − 1
```

**Market Sizing:**
- Top-Down: TAM × Addressable% × Reachable% × Share
- Bottom-Up: #Customers × Adoption% × AvgRev/Customer
- Always do BOTH. If they don't triangulate within 2–3x, re-examine.

### Common Traps

- **Boiling the ocean** — focus on what Q asks
- **Framework soup** — 1–2 per Q, not 5
- **Qualitative fluff** — "great team" needs evidence
- **Ignoring competition** — never analyze a market alone
- **Sustaining vs. Disruptive confusion** — better product for existing customers = sustaining; most products are
- **TAM/SAM/SOM mix-up** — TAM=total, SAM=addressable, SOM=obtainable
- **No P value** — if you can't ID the psychological dimension, commodity risk
- **Assuming problem awareness** — if customers don't know they have a problem, you must educate first

### Closing Principle

> Product launches fail for many reasons, including those out of your control, but you will ALWAYS fail if you don't focus on customer needs.
