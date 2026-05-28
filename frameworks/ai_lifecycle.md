# AI Across the Entrepreneurial Lifecycle

This framework — practical, opinionated, current as of 2026 — describes **when and how to use AI tools at each stage of the entrepreneurship journey**, what AI can and can't do, and the principles that separate transformative AI use from superficial AI use.

It is not a list of products. It is a method.

## The premise

Used badly, AI generates plausible-sounding slop that founders mistake for insight. Used well, AI compresses weeks of work into hours and surfaces patterns the founder would have missed.

The difference is not the tool. It is **the operator's discipline** — what questions to ask, what data to attach, what output to demand, and what to verify.

## The tool stack (2026)

A working AI operating system for a pre-PMF founder:

**Core LLMs**
- Claude (Anthropic) — Deep analytical work, long documents, complex reasoning, coding
- ChatGPT (OpenAI) — Broad tasks, coding, rapid iteration
- Gemini (Google) — Multimodal, Google workspace integration

**Productivity & Analysis**
- Notion — Knowledge management
- Read.ai — Meeting transcription and synthesis
- Gamma — AI-powered presentation design

**Development & Prototyping**
- Cursor — AI-powered code editor
- Claude Code — Command-line agentic coding
- Replit — Quick prototyping and deployment

**Visual & Research**
- Excalidraw — Diagrams
- Perplexity — Research with citations

The specific tools change quarterly. The discipline doesn't.

## The 8 meta-principles of AI use

These apply at every stage. Memorize them.

### 1. Context is king

The single most-leveraged input. More context = less guessing = less generic output.

**Bad prompt:** *"How big is the vertical farming market?"*

**Good prompt:** *"I'm an MBA-stage founder considering building software for mid-market (10K–50K sq ft) leafy-greens vertical farms in the US. I've talked to 15 farm GMs already. Help me synthesize what's structurally changing in the US CEA (controlled environment agriculture) industry over the last 2 years. Focus on changes that create or close opportunities for software vendors. Highlight what would surprise me. Cite where you're uncertain."*

### 2. Structure your requests

Clear structure = usable output, formatted correctly.

Examples of structure:
- *"Return as Markdown with H2 headers for each section."*
- *"Output a table with columns: Stakeholder | Their Pain | Their Workaround | What they'd pay."*
- *"Three sections: What I should keep doing. What I should stop. One new experiment to try."*

### 3. Role-setting changes quality

Primes the model to adopt a perspective and expertise level.

*"Act as a McKinsey partner who's worked on 15 controlled-environment agriculture deals."*

*"Act as a skeptical Series A investor who's seen 20 vertical farming pitches and decided not to invest in any of them. Ask the questions you'd ask the founder."*

### 4. Iterative refinement > perfect first try

AI is a collaborator, not a one-shot oracle. The pattern: generate first draft → critique → iterate → polish.

A useful chain: ask the model to **critique its own output.** *"Now read what you just wrote and tell me where it's vague or where you made things up."*

### 5. Chain of thought for complex tasks

Breaking tasks into steps improves quality and gives you control.

*"First, list the 5 stakeholder types I should reach. For each, identify their goals and what specific problems they'd talk about. THEN — based on that — propose 3 interview questions per stakeholder type that would surface non-obvious insights."*

The chain makes each step inspectable.

### 6. Ground in real data

Attaching real data prevents hallucination and ensures relevance.

Generic prompt produces generic output. Same prompt with *"I've attached the transcripts of 8 customer interviews. Use only these as the source for your synthesis. Where you make an inference, note which interview supports it."* produces specific, defensible output.

If you don't have data to attach, the AI will fill in with plausible-sounding patterns from training data — which are usually consensus and rarely useful.

### 7. Meta-instructions guide quality

Tell the AI how to think, not just what to think about.

Useful meta-instructions:
- *"If you're uncertain about something, say so explicitly."*
- *"State your assumptions before answering."*
- *"Stop and ask me a question if the prompt is vague."*
- *"Prioritize counterintuitive findings over easily Googleable ones."*
- *"Read this back and tell me what's the weakest part of your argument."*

### 8. Explicit output format

What format do you want the answer in?

Telling the model upfront — *"output as a 1-page PRD using the structure: Problem, ICP, Solution, Success metrics, Risks"* — produces copy-paste-ready content. Without explicit format, you get a wall of prose.

## Anti-patterns

The five most common AI misuse patterns:

1. **The vague open-ended question.** *"Tell me about vertical farming."* Output: generic and useless. Fix: specify context, output format, what you already know, and what you're trying to decide.

2. **Asking AI to predict the future.** *"Will AI replace vertical farms in 5 years?"* The AI does not know. It will produce a confident-sounding speculation. Fix: ask what factors would need to be true, not for a prediction.

3. **Treating output as final.** AI drafts are first drafts. Always review, edit, verify (especially anything external).

4. **Over-relying without verification.** When the AI cites something specific (a study, a stat), verify it independently. AI confidently hallucinates.

5. **Using AI for what it can't do.** AI cannot replace domain expertise, build relationships, or have judgment about high-stakes decisions you've gathered no data for. It can be a great research assistant; it is not a strategist.

## By stage — when and how to use AI

### Stage 00 — Prepared Mind / RDI

**What AI is great for:**
- Building the industry primer (faster than manual reading). Use Deep Research mode in Claude/ChatGPT.
- Mapping ecosystem players and stakeholder relationships
- Generating interview question pools for different personas
- Cross-interview pattern recognition after 5+ interviews
- Reframing 2x2s — quickly trying different axes
- Drafting outreach emails (tailored per persona)

**What AI cannot do here:**
- The actual interviews — humans needed
- Build relationships with stakeholders
- Identify what's *truly* counterintuitive in your space — that comes from the conversations

**Critical discipline:** the primer is **for you, to prepare for primary research.** It is not a deliverable, not a thing to share publicly, and not validated knowledge. Use it to ramp up — then immediately go talk to humans. If you can defend the synthesis only by referring back to AI output, you haven't learned it.

### Stage 01 — Insight and Idea Selection

**What AI is great for:**
- Drafting your opportunity rubric (then editing)
- Brainstorming candidate insights (then critiquing them)
- Pressure-testing your insights against the consensus filter — *"Tell me three sophisticated people in this space who would disagree with the insight: [X]."*
- Generating bull and bear cases for candidate opportunities

**What AI cannot do here:**
- Judge whether your insight is *non-consensus.* That requires conversations with informed people.
- Tell you whether the inflection is real or imagined.

### Stage 02 — Customer Discovery

**What AI is great for:**
- Designing interview scripts (then editing for your specific hypothesis)
- Post-interview synthesis from transcripts (use Read.ai → Claude pipeline)
- Cross-interview pattern recognition
- Stakeholder/persona mapping
- Building a hypothesis tracker

**What AI cannot do:**
- The interviews themselves
- Detect when an interview is being poisoned by the interviewer's leading
- Replace the Mom Test discipline

**Pattern that works:**
- Transcribe with Read.ai
- Send transcript + your hypothesis to Claude with: *"Tag every place this customer described a workaround they've built. Tag every place they mention spending money on the problem. Tag every place they mention emotion. Tag every place they offered an opinion vs. described past behavior. Then summarize what desperation markers (if any) this person exhibits."*

### Stage 03 — Problem-Solution Fit

**What AI is great for:**
- Drafting candidate solution shapes (then critiquing them)
- Sketching unit economics scenarios
- Drafting landing pages / concept-test artifacts
- Generating "would this work?" red team analysis on each shape

**Caution:** AI will help you make a beautiful concept test. The concept test still needs to be shown to real customers.

### Stage 04 — Value Hypothesis

**What AI is great for:**
- Pressure-testing the *who* — *"Read this customer description. Tell me 5 ways it's too broad. Then 5 ways it could be narrowed further."*
- Surfacing leap-of-faith candidates — *"Read this value hypothesis. What is the single most important behavioral assumption it depends on?"*
- Red-teaming the hypothesis — *"Argue why this hypothesis will fail. What would have to be true for the failure scenario?"*

### Stage 05 — MVP Build

**What AI is great for:**
- Coding the MVP (Cursor, Claude Code, Replit) — especially for non-technical founders
- Drafting onboarding flows
- Generating test plans, user flows
- Triaging bugs and edge cases
- Drafting customer success copy and FAQs

**What AI cannot do:**
- Decide what to build (that's your judgment about the leap of faith)
- Watch customers use the product
- Get real desperation feedback

### Stage 06 — PMF Measurement

**What AI is great for:**
- Analyzing retention curves, cohort patterns
- Drafting the Sean Ellis survey
- Synthesizing NPS comment boxes
- Identifying the over-performing slice in your data (use the chain-of-thought prompt: "look for any segment where retention/conversion/engagement is 2x+ the average; tell me what's distinctive about that segment")
- Drafting an honest PMF status update for the team

### Stage 07 — Pivot or Persevere

**What AI is great for:**
- Drafting the pivot memo
- Pressure-testing the new value hypothesis
- Red-teaming the perseverance argument
- Generating "what would change my mind" tests

**What AI cannot do:**
- Make the decision. The decision is the founder's. (But running both the bull and bear arguments through AI is a useful way to ensure you've heard them.)

## The "verify everything important" rule

When AI cites a specific stat, study, or fact, **verify it independently before using.**

The hallucination problem is real:
- AI cites studies that don't exist
- AI cites real studies with wrong numbers
- AI cites recent news that's outdated
- AI cites things that "sound right" but aren't checked

The fix:
- Demand source URLs
- Use web-search-enabled AI (Perplexity, Claude with web search) when current data matters
- Triangulate across multiple AI systems
- Verify key claims with primary sources

A useful test: if a stat is **specific** (e.g., "94.7% reduction in waste"), be suspicious — those are exactly the kinds of numbers AI fabricates. If a stat is round and citation-free, also be suspicious.

## When AI doesn't help

There are entrepreneurial tasks where AI doesn't help — and you should know which:

| Task | Why AI doesn't help |
|---|---|
| Building genuine relationships | Trust is built through real interaction |
| Identifying *truly* counterintuitive insights | AI is trained on consensus content |
| Domain expertise in highly regulated spaces | Compliance specifics need human verification |
| High-stakes judgment calls | The decision is yours; AI gives input |
| Negotiation | Real-time human reading |
| Customer support that affects retention | Empathy, judgment, escalation paths |
| Founder energy and conviction | Cannot be outsourced |

The right framing: AI is a great *research assistant, drafter, synthesizer, and verifier*. It is **not** a *founder, customer, or judge.*

## A note on AI in 2026

Where we are:
- 2022–2023: ChatGPT moment. Consumer AI mainstream. Mostly writing assistance.
- 2024: Capability explosion. Reasoning, multimodal, long context, early agents.
- 2025–2026: Inflection point. AI-native companies emerging. Traditional businesses racing to integrate. Competitive advantage shifting to AI leverage.

What this means for founders: **using AI well is now a baseline competency**, not a differentiator. The differentiation comes from:
- Asking better questions
- Bringing better data
- Verifying outputs ruthlessly
- Combining AI with the human work (interviews, judgment, relationships) it can't do

Founders who treat AI as a magic answer machine produce slop. Founders who treat AI as a brilliant-but-fallible research assistant produce a 3–10x productivity edge.

## Where this lives in the journey

- Every stage. The framework applies throughout.
- [`playbooks/synthesis.md`](../playbooks/synthesis.md) — AI-assisted synthesis methods
- [`playbooks/build_industry_primer.md`](../playbooks/build_industry_primer.md) — AI-assisted primer
- [`playbooks/run_outreach.md`](../playbooks/run_outreach.md) — AI-assisted outreach

## Source

Synthesized from the "AI Across the Company Lifecycle" Notion guide (alex-kalyvas-kasopatidis, 2025–2026) and the practice patterns embedded in Stanford's STRAMGT 546 (RDI) AI Toolbox section. Updated for 2026 tooling.
