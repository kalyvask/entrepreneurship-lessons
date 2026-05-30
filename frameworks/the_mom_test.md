# The Mom Test (Rob Fitzpatrick)

> Rob Fitzpatrick's premise, and the source of the name: structure your questions so that even your mom — who wants to support you — couldn't mislead you about your idea.

The most useful 80-page book in customer development. The premise: **everyone you talk to about your idea will lie to you.** Not deliberately. Out of politeness, ignorance, or kindness. Even your mother — who loves you — will tell you she'd buy your app even when she wouldn't.

The book is a discipline for **extracting honest information from biased conversations**, by structuring the questions so that even the most polite, well-intentioned interlocutor cannot mislead you without effort.

## The premise

Customers are not lying because they want to mislead. They are lying because:

1. **They are being polite.** Saying "no, that's a stupid idea" feels rude. Saying "yes, sounds great!" feels supportive. Most people pick supportive.
2. **They don't know what they'd do in the future.** Asking "would you use this?" requires them to predict their own behavior in a hypothetical situation — and humans are reliably bad at this.
3. **They want to be helpful.** They generate ideas, suggestions, features — not because they need them but because they want to participate.
4. **Compliments cost them nothing.** Saying "I'd totally pay for that" is socially free. Actually paying is not.

The book's discipline gets around these biases by **focusing on the past, not the future**, on **their life, not your idea**, and on **specifics, not generics**.

## The three rules

### Rule 1 — Talk about their life, not your idea

The worst version of a customer conversation: *"So here's our idea. We're building [X]. What do you think?"*

The interviewer pitches. The interviewee listens and reacts to the pitch. Everything from that point forward is poisoned — they're commenting on the pitch, not their reality.

The right version: *"Tell me about how you currently handle [problem area]."* Or *"What's the most frustrating part of [activity] for you right now?"*

This invites stories about their real life. The data is honest because it's about a past you don't control.

### Rule 2 — Ask about specifics in the past, not generics or opinions about the future

The most common interview mistake: asking about the future.

- *"Would you use a tool that does [Y]?"*
- *"How much would you pay for [Z]?"*
- *"If we built [X], would you switch?"*

These questions sound reasonable. They produce useless data. Stated future intent has very low correlation with actual future behavior.

The fix: convert every future question into a past question.

- *"Tell me about the last time you tried to [Y]."*
- *"What have you paid for in the past to solve [Z]?"*
- *"What did you switch *to* when you last replaced your previous tool?"*

The past has a fact pattern. The future has a story. Facts are more useful than stories.

### Rule 3 — Talk less, listen more

The 90/10 rule: you talk 10% of the time. The interviewee talks 90%.

Specifically:
- **Don't fill silences.** Silence is generative. The most important answers often come *after* a pause that feels uncomfortable to you but is productive for them.
- **Don't pitch.** Even when they ask "so what is your idea?" — answer briefly, then redirect: *"I'd love to show you in a bit. But first — tell me more about how you're doing it today."*
- **Don't lead.** Don't say "we're thinking about doing X." Don't say "would it help if..."
- **Don't seek validation.** Don't say "does that sound useful?" *Validation-seeking is the most common subtle form of self-poisoning.*

## What good signal looks like

| ✅ High signal | ❌ Low / no signal |
|---|---|
| A specific story about a past event with names, dates, and outcomes | "I think it'd be useful" |
| A workaround they've already built or commissioned | "I might want it" |
| A reference to spending budget on this problem already | "We've thought about that" |
| Emotion — frustration, anger, excitement — when describing the problem | Polite nods |
| Unprompted mention of the problem before you bring it up | They say it sounds great but the conversation moves on |
| A request to keep them updated, paired with action ("introduce me to your CTO") | A request to keep them updated, with no action |
| An offer to introduce you to others with the same problem | "I'll think about it" |
| Volunteered details they wouldn't have shared unless the pain was real | Generic descriptions of their workflow |

The general pattern: **specifics about the past are signal. Generics about the future are noise.**

A two-sentence diagnostic. After every conversation, ask yourself: *"What does this person currently do, and what would have to be different about their current behavior for our product to capture value?"* If you can't answer either part from the conversation alone, the interview was probably poisoned by your own leading.

## Compliments are the bane of a learning startup

Fitzpatrick is sharp on this. Compliments — *"That's a great idea!"* — feel validating. They are actually evidence that you are leading the conversation. **A well-conducted Mom-Test conversation should feel slightly uncomfortable**, because you are repeatedly redirecting the interviewee back to their life from your idea.

If every conversation ends with the interviewee being excited about your idea, you are almost certainly pitching, and the data is corrupted.

## Specific question reformulations

A library of common mistakes and their fixes. Use this as a self-edit checklist before any interview.

| Bad (Future / Opinion / Leading) | Good (Past / Behavior / Open) |
|---|---|
| "Would you use this?" | "How are you currently handling [problem]?" |
| "Would you pay $X for this?" | "What have you paid for in the past to solve this?" |
| "Do you think the design is intuitive?" | "Show me how you'd accomplish [task]." |
| "What features should we add?" | "Tell me about a time the current solution failed you." |
| "Is this useful?" | "What did you do the last time this happened?" |
| "Do you have this problem?" | "Walk me through the last time you tried to [task]." |
| "Who else should we talk to?" | "Who else struggles with this? Mind making an intro?" |
| "What do you wish existed?" | "What workarounds have you built for this?" |
| "How big a problem is this?" | "How often does this come up? What did it cost you the last time?" |
| "Would you tell your friends about this?" | "Tell me about the last tool you recommended to a coworker. Why that one?" |

## Three commitments and three signals

Fitzpatrick frames the goal of a great customer interview as eliciting **commitment and concrete advancement** rather than reassurance.

**Three commitments** (in order of strength):
1. **Time** — they will come back for a follow-up conversation, see a demo, give you 30 more minutes.
2. **Reputation** — they introduce you to someone (their boss, a peer, a customer of theirs).
3. **Cash** — pre-pay, LOI, deposit, signed pilot agreement.

**Three signals** that the conversation is real (vs. polite):
1. They **bring up the pain unprompted.**
2. They **describe a workaround** they've already invested in.
3. They **want it now** — first reaction is "When can I have it?" not "Maybe in Q3."

A great interview produces at least one of the three commitments and at least one of the three signals. A polite interview produces neither.

## Customer slices and the rule of three

A second-order discipline: customers are not monolithic. You'll have conversations with people who *seem* like they fit your target customer but actually behave very differently from each other.

Fitzpatrick's rule: **if the same insight comes up in three independent conversations with different people across different organizations, that's a pattern.** Less than three, it's anecdote. More than three, it's signal.

Same in reverse: **if a particular request comes from only one customer, don't build for it.** Even if that customer is excited, even if they offer to pre-pay. One enthusiastic customer is not a market.

## When the conversation goes wrong

Symptoms of a poisoned interview:

- You're talking more than them.
- They're complimenting your idea.
- They're suggesting features.
- They're agreeing that the problem you described is a problem.
- You leave feeling great.

The fix in the moment: **redirect to a past behavior question.**

- "Tell me about the last time this came up."
- "How did you handle it?"
- "Show me what you did."

The fix between interviews: **review the script before the next one.** Cut every word of pitch. Cut every "would you...". Cut every "do you think...". Replace each one with a past-tense, specific, behavioral question.

## The connection to Rachleff and Blank

Fitzpatrick's three rules align tightly with what Rachleff calls *desperation testing* and what Blank calls *getting out of the building.*

- **Blank**: get out and talk to customers.
- **Fitzpatrick**: here's how to talk to them so the data is honest.
- **Rachleff**: here's what to listen for (the four desperation markers).

All three together: discipline for the most important conversations of your startup's life.

## Where this lives in the journey

- [Stage 00 — Prepared Mind](../stages/00_prepared_mind.md) — RDI interviews
- [Stage 02 — Customer Discovery](../stages/02_customer_discovery.md) — the heaviest user of Mom Test discipline
- [Stage 03 — Problem-Solution Fit](../stages/03_problem_solution_fit.md) — concept-test conversations
- [Stage 07 — Pivot](../stages/07_pivot_or_persevere.md) — diagnosing why current customers aren't desperate

## Source

*The Mom Test: How to talk to customers & learn if your business is a good idea when everyone is lying to you* — Rob Fitzpatrick (2013, self-published, ~80 pages). The shortest, most useful book on customer development in print. Required reading for any founder before their first customer conversation.
