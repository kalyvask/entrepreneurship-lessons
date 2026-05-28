# Stage 02 — Customer Discovery

> *"Customer development is selling people what you have and learning from their reaction. Market research is asking people what they want. They are categorically different."* — paraphrased from Steve Blank, via Andy Rachleff

This is the stage where most ideas die — and most should.

The job of customer discovery is **not** to convince customers to buy. It is **not** to validate that you are right. It is to find out who, if anyone, is *desperate* enough for what you'd build to behave like a desperate person — to spend money on a half-built version of it, to forgive bugs, to recruit others, to talk about it unprompted.

You will, in this stage, talk to a lot of people who say polite, encouraging, non-buying things. **Polite encouragement is the worst possible signal**, because it feels validating without being predictive. You will train yourself to distrust politeness and trust behavior.

## When you are in this stage

- You have an insight (from [Stage 01](01_insight_and_idea.md)) — a defensible non-consensus belief about how a market or technology is changing.
- You have hypotheses about *who* might be desperate for what the insight implies.
- You have not yet built a product. You may have a concept, a wireframe, a prototype, but no MVP.
- You are doing 20–80 customer-facing conversations.

If you have an MVP and live users, you are in [Stage 05 — MVP build and test](05_mvp_build.md) or [Stage 06 — Validation and PMF measurement](06_pmf_measurement.md).

## What "good" looks like at the end of this stage

- You have a **clear picture of who is desperate** — not who is "interested" or "needs help" but who exhibits the four desperation markers (below).
- You can describe this customer in a sentence so specific that you could *manually identify 50 of them today.* "Mid-market vertical-farm general managers, 10–50k sq ft, leafy greens" — not "operators in agtech."
- You have **named the job** they are hiring you to do. (JTBD: see [`frameworks/jobs_to_be_done.md`](../frameworks/jobs_to_be_done.md).)
- You have catalogued the **alternatives they currently use** — including DIY workarounds, spreadsheets, internal tools, consultants. Especially the workarounds; those are the strongest desperation signals.
- You have evidence that this customer would **pay** (or pre-pay, or sign a letter of intent, or do something that costs them something) before you build the full product.

## The desperation markers

> *"Need is irrelevant. Desperation is everything."* — Andy Rachleff

Rachleff has lived with this claim for 45 years. The marketing language for "desperation" varies — some people prefer "burning problem", "hair-on-fire pain", "must-have problem" — but the operational test is the same. A desperate customer is identified by **behavior**, not by what they say. Stated preferences are nearly useless; observed behavior is dispositive.

The four markers:

**1. They are willing to pay with little proof.**
A desperate customer does not ask for 50 references. They see the product work once and they want it. *"When can I have it?"* They prepay, they take the pilot, they sign the LOI before they've seen the final pricing.

**2. They have tried to build the solution themselves.**
The single strongest signal in enterprise. The engineering team has a janky Python script. The ops team has a 47-tab Excel sheet. The IT team has hired a contractor. *They have already spent money or time on this problem.* That's behavior. That's desperation.

**3. They mention the pain unprompted.**
You don't have to set up the conversation. They bring it up. They have a story about how it screwed up their last quarter. The pain is alive in their head, not something you have to remind them of.

**4. They want it now, not next quarter.**
Their first reaction is *"How quickly can we get it?"* — not *"Let's set up a pilot review in Q3."* If they're scheduling a pilot evaluation against your competitors, they are pragmatist not visionary, and pragmatists do not buy MVPs from unknown companies.

A customer who exhibits 3–4 of these is a desperate customer. 1–2 is a "needy" customer who will waste your time. 0 is a customer who is being polite.

## What this stage is NOT

It is not a focus group. It is not a survey. It is not a brainstorming session with friends. It is not running ads to see what resonates.

It is also **not pitching**. The moment you pitch, two bad things happen: the person either gets guarded (and you learn less than you would have), or they get polite (and you walk away thinking you've validated something when you've validated nothing). See [`frameworks/the_mom_test.md`](../frameworks/the_mom_test.md) for the discipline.

The interview model is **forward-from-curiosity, backward-from-evidence**. You are listening for stories about the past — concrete things that have happened — not opinions about your idea. Stories about the past are honest; opinions about the future are mostly garbage.

## The customer development sprint

A working pattern for this stage:

### Week 1–2 — Identify the hypothesized customer

- From your insight, list 3–5 candidate *who*s — different customer segments that might experience the problem most acutely.
- For each: how would I find 50 of them today? If you can't name a search strategy that works, the segment is too vague.
- Pick one to focus on first. Don't run all 3–5 in parallel — you'll dilute attention and miss the patterns within any one segment.

### Week 2–4 — Run 15–20 conversations in the focus segment

- 30 minutes each. (Sometimes 45 — but the discipline of 30 forces you to skip pleasantries.)
- The interviewee is the expert. You are there to learn.
- Open-ended questions. No leading. (See playbook below.)
- Record (with consent) and transcribe. Words matter; paraphrased notes lose nuance.
- Take separate notes during ("inside" notes — what they said), and a debrief immediately after ("outside" notes — what you noticed, surprises, where emotion showed up).

### Week 4–5 — Synthesize and pressure-test

- Cluster the pain points (Pile Building / Cluster Analysis — see [`playbooks/synthesis.md`](../playbooks/synthesis.md)).
- Map each candidate problem against the desperation markers. Mark behavior, not stated preference.
- Identify the **3–5 sharpest patterns** that recur across multiple conversations.
- For each: *can I name a specific person from the conversations who exhibits 3+ desperation markers for this problem?* If yes, you have signal. If no, you have a problem but not a desperate customer.

### Week 5–6 — Narrow

Narrowing is the most counterintuitive move in this stage. Founders want to keep options open. The course is unambiguous: **you cannot test what you haven't narrowed to.**

The Wealthfront example — the way Andy Rachleff describes how narrow is narrow enough:

1. Young people in tech — too broad
2. Engineers in tech companies — still too broad
3. Engineers in tech companies about to go public
4. Engineers in *consumer-focused* tech companies about to go public
5. Engineers in consumer-focused tech companies about to go public, with under $1M in assets, who were reluctant DIY index investors

Level 5 is targetable. *"I can literally pick those people. I can manually go after them."*

If you can't picture going to a specific person's LinkedIn and saying *"this is one of them"*, you have not narrowed enough.

## The interview discipline (The Mom Test)

Rob Fitzpatrick's *The Mom Test* is required reading. The book's premise: **even your mother — who loves you — will lie to you about your idea if you let her.** People do not lie deliberately; they lie out of politeness, ignorance about their own future behavior, and a misunderstanding of what kind of feedback you actually need.

Three rules Fitzpatrick gives:

**1. Talk about their life, not your idea.**
Ask about their past behavior. *"Tell me about the last time you tried to do [X]"* gives you a story. *"Would you use a tool that does [Y]?"* gives you a hypothetical and they will lie politely.

**2. Ask about specifics in the past, not generics or opinions about the future.**
*"How did you handle [problem] last quarter?"* is gold. *"Do you think you'd want a solution for [problem]?"* is garbage.

**3. Talk less, listen more.**
The 90/10 rule (you talk 10% of the time). Especially: don't fill silences. The most important answers often come after a pause that feels uncomfortable to you but generative to them.

What to listen for:
- **Specifics** (a real story, with names, dates, dollar amounts) — high signal
- **Hypotheticals** (*"I might…", "I'd probably…", "It depends…"*) — low signal
- **Emotion** (frustration, anger, excitement) — high signal
- **Workarounds** they've already built — extremely high signal
- **Compliments about your idea** — zero signal (in fact, suspicious — see Fitzpatrick on "compliments are the bane of a learning startup")

Compare:
- 🟢 *"Last quarter we lost 47 hours to manual reconciliation. We hired a contractor to write a script. It half worked. I'd pay $5k a year for something that actually solved this."* (Specific past behavior, named problem, named workaround, named willingness to pay.)
- 🔴 *"Yeah, this sounds really useful. We have a lot of problems with that. You should definitely build it."* (No specifics, no past, no behavior.)

The second response *feels* better than the first. It is much worse.

## How many is enough?

The traditional advice — "5 to 8 interviews surfaces 80% of usability issues" — is for design research. For customer discovery, the math is different. **Most teams stop at 20 because they're hearing the same things. The same things at 20 are surface. Depth shows up at 40–60.** Pattern recognition gets better the more you stack. The 50th interview is dramatically more valuable than the 5th because you bring more context to it.

If you can't run that many in a focused segment, your segment is too narrow or your sourcing is broken — that's also a finding.

## Saying "no" to people who want you to build for them

A specific failure mode worth naming. As you talk to people, some will get excited. Some will offer to be your design partner. Some will say *"if you just added this feature, I'd buy it."*

This is where most teams die.

**Adding features in response to lukewarm customers is what Rachleff calls "lunacy."** If the customer was not desperate before the feature, the feature does not make them desperate. They will ask for more features, and more features, and you will run out of money building a product for someone who doesn't actually want it.

The discipline:
- Note the request.
- Check the desperation markers for that customer. If they don't have 3+, do not modify the product to accommodate them.
- If the same feature comes up from 5+ unprompted, then it's signal. (But even then: ask whether you should change the *who* — find customers who don't need that feature — before changing the *what.*)

## Common failure modes in this stage

| Failure | What it looks like | Why it kills you |
|---|---|---|
| Talking to friends | Easy to schedule, easy responses | Friends will be polite; you'll get false-positive signal |
| Pitching, not probing | Slides, demos, "what do you think?" | Interviewees adapt to what they think you want to hear |
| Asking about the future | "Would you use…?" "Would you pay…?" | Stated future intent is unreliable; ask about past behavior |
| Talking to whoever responds | Anyone with a pulse | You're filling the schedule, not finding the desperate customer |
| Stopping at 20 | "I'm hearing the same things" | You haven't reached the depth of pattern yet |
| Falling in love with one excited prospect | "This one VP loved it, let's build for them" | One excited prospect ≠ a market; their desperation may be idiosyncratic |
| Not narrowing | "We could sell to mid-market and enterprise" | You can't test what you haven't narrowed to |
| Compliment fishing | Walking away from a call feeling validated | Compliments are zero signal; the conversation should have been *uncomfortable* |
| Building before validation | "We need to show them something" | A wireframe is fine. An MVP is too expensive to build for a customer who isn't desperate yet. |

## Exit criteria — leaving this stage

You can move to [Stage 03 — Problem-Solution Fit](03_problem_solution_fit.md) when:

1. You can describe the customer in one sentence narrow enough to manually identify 50 of them.
2. You can list 3+ desperation markers exhibited by at least 5 different people in that customer segment.
3. You have at least one example of someone in that segment who has *built a workaround* — a real, observed thing, not a story.
4. The problem you'd solve recurs unprompted across the conversations.
5. You can describe the alternatives they currently use, including DIY, and why those don't fully work.
6. You have specific names of 3–5 people who said "show me what you have, I want to use it."

If you can't get to all of these — you have a *needy* market, not a *desperate* one. That's a kill signal. Go back to Stage 00 or 01, look at the other candidates from your insight, and pick another segment.

## Required reading

- [`frameworks/the_mom_test.md`](../frameworks/the_mom_test.md) — interview discipline
- [`frameworks/customer_development.md`](../frameworks/customer_development.md) — Steve Blank's methodology
- [`frameworks/jobs_to_be_done.md`](../frameworks/jobs_to_be_done.md) — JTBD framework for understanding what customers are actually "hiring" a product to do
- [`playbooks/customer_interview.md`](../playbooks/customer_interview.md) — full interview playbook
- [`playbooks/synthesis.md`](../playbooks/synthesis.md) — turning conversations into clusters and patterns
- [`templates/interview_script.md`](../templates/interview_script.md) — interview script template

## Agent partner

- `/ent-interview-prep` — Pre-interview prep including specific questions for your hypothesis
- `/ent-interview-debrief` — Capture findings immediately after; identifies desperation markers, signals, and gaps
- `/ent-customer-discovery` — Tracks your conversations across the sprint; surfaces patterns; flags when you're talking to needy vs desperate customers
