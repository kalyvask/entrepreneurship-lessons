# Synthesis Playbook

Synthesis is the bridge between exploration and clarity. By itself, raw interview data is noise. Synthesis is the discipline that turns N conversations into a thesis.

**The mindset:** synthesis is a **thinking exercise, not a deliverable.** You're not building beautiful slides; you're working with material until patterns reveal themselves.

## The arc of synthesis

Synthesis evolves through your research:

- **Early synthesis** — organizing and noticing. What topics recur? What language do people use to describe the same thing?
- **Mid synthesis** — pattern recognition and stakeholder comparison. How do executives describe a problem versus operators? Where do multiple independent sources point to the same tension?
- **Late synthesis** — testing and pressure-testing. Can you articulate why you believe what you believe? What would change your mind?

The temptation at each phase: force clarity too early. The discipline: **stay confused until clarity emerges from the material.**

## The five methods

In rough order of when you use them.

### 1. Pile Building (Input Breakdown)

**What it is:** convert each source — an interview, an article, a report — into discrete, tagged scraps. Each scrap is one observation, one quote, one pattern.

**Why it works:** working with scraps lets you move ideas physically. You see contradictions. You see patterns. You see gaps.

**How to do it:**

1. Open one interview transcript
2. Read through. As you go, copy out **discrete scraps**:
   - A quote
   - A behavior they described
   - A workaround they mentioned
   - A piece of data
   - A frustration they expressed
3. Tag each scrap with: source (who said it), category (whatever's emerging), and confidence (high if specific past behavior, low if hypothetical opinion)
4. Move on to the next source

You can do this on paper, in a Notion/Airtable table, in a Miro board, or with AI:

> *"Here's the interview transcript. Extract every distinct observation as a scrap. For each scrap include: the exact quote, who said it, what category it fits, and whether it's about past behavior (high signal) or future opinion (low signal). Output as a table."*

After 5–10 interviews you should have 50–150 scraps.

### 2. Cluster Analysis

**What it is:** group accumulated scraps into distinct, **active** claims.

**The rule for cluster names:** name them as **insight statements, not categories.**

- ❌ "Data Issues" — generic
- ✅ "Data exists, but no one trusts it" — active

- ❌ "Sales Cycle"
- ✅ "Sales cycles stall at the IT review, not the business decision"

- ❌ "Worker Management"
- ✅ "Hourly workers churn at 200% annual; managers feel powerless to fix it"

The act of naming forces you to articulate what you actually see, not what's nearby.

**How to do it:**

1. Spread the scraps out
2. Find 2–3 scraps that go together. Name the cluster as an insight statement
3. Find more scraps that fit. Move them in
4. Some scraps will be ambiguous. Park them
5. Some clusters will overlap. That's okay — note the overlap; it's signal
6. When you've placed most scraps, look at the clusters and the unparked
7. **Tensions between clusters are signal, not noise.** Cluster A says "X" and Cluster B says "the opposite of X." That's a real disagreement in the space. Probe it.

After clustering, you should have 8–15 clusters with active names. The names are your draft insights.

**Re-cluster as you accumulate more material.** Clusters that made sense at 30 scraps may need to break apart at 80 scraps as more detail surfaces.

### 3. Mapping and Process Diagrams

**What it is:** visual diagrams of who does what in the space — value chains, workflows, regulatory flows, data flows.

**Why it works:** specific dependencies become visible. Bottlenecks reveal themselves. Switching costs and incentive misalignments emerge.

**How to do it:**

1. Pick one core process or value chain you've heard about across interviews
2. Sketch it — who's involved, what flows between them, where money and data move
3. Layer in friction points you've heard about (from clusters)
4. Layer in timing/regulation/technology that affects the flow
5. Look for **tensions in the system** — control vs. flexibility, growth vs. margin, centralization vs. decentralization

**Tool:** Excalidraw, Miro, FigJam, or paper. Don't over-engineer. The thinking is in the sketching, not in the polish.

### 4. Attribute Maps and 2x2 Frameworks

**What it is:** plot the players, products, or customer segments along two dimensions to reveal structure.

**The first axes are rarely the best.** The real insight comes on iteration 2 or 3 when you find a framing that makes the landscape *snap into focus.*

**How to do it:**

1. Pick two dimensions you've heard about (price/quality, scale/specialization, technical/relational, etc.)
2. Plot the players/segments you've heard about
3. Look for structure: are there clusters? Empty quadrants? Lines?
4. **Try different axes.** Many. AI helps here:

> *"For mid-market vertical farms, suggest 8 different pairs of axes that could be used to segment them. For each pair, briefly describe what the four quadrants would represent and whether you'd expect a cluster pattern or a continuum."*

5. Iterate until the framing makes the landscape obvious

A good 2x2 produces an **empty quadrant** that's revealing — *"no one is serving this corner; that's the opportunity"* — or a **boundary** along the diagonal that explains who succeeds vs. fails.

### 5. Stakeholder Comparison

**What it is:** lay perspectives side by side. Executives, operators, investors, regulators, customers describing the same industry through different lenses.

**Why it works:** disconnects between stakeholder types are usually signal, not noise. The places where perspectives diverge most sharply often point to the most interesting opportunities: misaligned incentives, unrecognized pain points, blind spots created by where someone sits.

**How to do it:**

1. Pick a topic you've heard multiple stakeholder types discuss
2. Make a comparison table:

| Stakeholder | How they describe X | What they want | What they're scared of | What surprised me |
|---|---|---|---|---|
| Operator | ... | ... | ... | ... |
| Investor | ... | ... | ... | ... |
| Regulator | ... | ... | ... | ... |

3. Where the rows diverge most = where the opportunity often lives
4. Tag specific divergences as candidates for further research

### 6. Hypothesis Tracking

**What it is:** a running list of explicit hypotheses with supporting evidence, contradicting evidence, and confidence level.

**Why it works:** keeps you honest. Distinguishes patterns that are real (six independent sources without prompting) from patterns you want to be real (two enthusiastic interviews and a gut feeling).

**How to do it:**

A shared doc with these columns:

| Hypothesis | Stated By | Supporting evidence | Contradicting evidence | Confidence | What would change my mind |
|---|---|---|---|---|---|
| Mid-market farms can't justify >$2k/mo software | 3 GMs, 1 CFO | $1.5–2k current ad-hoc spend; tight P&L | None yet | Medium | One GM pre-paying $4k/mo |

Review the list weekly. Some hypotheses gain weight. Others collapse. Both are progress.

## Writing as synthesis

Not all synthesis is visual. **Writing forces you to confront what you actually know vs. think you know.**

Three formats:

**Living primer** — keep updating it through Phase 3 of RDI. New information slots in or reshapes the structure. Gaps become prompts for additional exploration. See [`playbooks/build_industry_primer.md`](build_industry_primer.md).

**Memos and briefs** — concise (1–2 pages), focused write-ups. A memo captures themes from a cluster of interviews or a pattern across stakeholders. A brief is more hypothesis-driven — reframing a problem or making the case for a deep dive.

**White papers and thought pieces** — more time-intensive, more comprehensive. Build credibility with serious stakeholders.

*These documents don't need to be perfect. They're tools for thinking. If something is hard to write, that's usually a sign you need to think about it more.*

## AI in synthesis

AI fundamentally changed what's possible. You can try three clustering approaches in the time it used to take to do one. Re-cut a 2x2 with different axes in minutes. Re-segment by stakeholder type or geography. Ask AI to identify themes you might be missing across dozens of interview transcripts.

**The discipline:** stay in the driver's seat. Use AI to prepare inputs, generate alternative groupings, pressure-test conclusions, and extend thinking. But *you* form the perspective.

**The test:** if you can explain what you're seeing and why it matters *without referring back to what the AI generated*, you've done real synthesis.

Useful AI prompts:

**Pile building:**
> *"Here's interview transcript [N]. Break it into discrete observations. For each, give me the quote, the implicit pain or need, and whether it's about past behavior (high signal) or future opinion (low signal). Output as table."*

**Cluster generation:**
> *"I've attached 60 scraps from 8 interviews. Suggest 6–10 clusters that group them. Name each cluster as an active insight statement — not a category. Highlight tensions between clusters."*

**Cross-interview patterns:**
> *"I've attached 12 customer interview synthesis docs. Find patterns that appear across 3+ interviews. For each pattern, list which interviews support it and which (if any) contradict it. Don't make up patterns — only ones with explicit support."*

**Stakeholder comparison:**
> *"I have interviews with 4 GMs, 3 investors, 2 academics, and 2 regulators. For each of these topics — [topics] — how do their perspectives diverge? Output as comparison table."*

**2x2 ideation:**
> *"For mid-market vertical farms, suggest 8 different pairs of axes that could be used to segment them. For each pair, briefly describe what the four quadrants would represent."*

## When synthesis is working

Signs you're on track:

- You feel *more* confused than when you started 2 weeks ago
- Clusters keep needing to be re-named because new material reframes them
- You hear someone in an interview say something and you *know* it's a pattern, not an outlier
- You start anticipating what an interviewee will say before they say it
- You find yourself caring about whether you're right — *I want to know*, not *I want to be validated*

When synthesis is broken:

- Clusters with generic names ("Data Issues") — you haven't articulated the insight
- Every conversation feels like a new pattern (you haven't found the structure)
- You have a thesis you protect, and incoming data either supports it or "doesn't apply"
- You can't tell a friend the most surprising thing you've learned in plain English

## Where this lives in the journey

- [Stage 00 — Prepared Mind](../stages/00_prepared_mind.md) — RDI Phase 3 synthesis
- [Stage 02 — Customer Discovery](../stages/02_customer_discovery.md) — synthesis after each batch of interviews
- [Stage 06 — PMF Measurement](../stages/06_pmf_measurement.md) — synthesis of usage data + interview signal
- [`frameworks/rdi.md`](../frameworks/rdi.md) — RDI's synthesis discipline

## Source

Stanford GSB STRAMGT 546 (RDI) — particularly Session 7 (Pile Building + Cluster Analysis) workshop materials. Brady/Jordan. The 2x2 / stakeholder comparison / hypothesis tracking patterns are standard in strategy and design research; RDI's contribution is the discipline of "active insight" cluster naming and the explicit rule that *tensions are signal.*
