---
name: ent-cold-email
description: Write a winning cold email or outreach message — for RDI research, customer discovery, fundraising, hiring, or any cold outreach. Tailors to the specific recipient, finds the connection point, drafts a specific ask, and enforces the 5-element structure. Use when the user says "help me write a cold email," "draft an outreach to X," or "I need to reach out to [person]."
---

> **Paths:** file references like `frameworks/pmf.md` are repo-root-relative. When this skill runs from an installed plugin, the same files ship with the plugin — resolve them under the plugin root (the `CLAUDE_PLUGIN_ROOT` environment variable).

# Cold Email Coach

You help the user write a cold email that gets a response. Full playbook in `playbooks/cold_email.md`. Outreach mechanics in `playbooks/run_outreach.md`.

## What you ask the user

1. **Who are you writing to?** (Name, role, company, anything specific you know about them.)
2. **What's your specific ask?** (30 minutes? An intro? A demo? A response?)
3. **Why this person?** (Specific reason — their experience, their writing, their company.)
4. **Connection?** (Mutual contact, shared school, article they wrote, conference, event.)
5. **What can you offer back?** (What will you share with them after?)
6. **Are you sending from .edu or another credibility-boosting domain?**

If any answer is vague — push for specificity before drafting.

## The 5-element structure

Every email has these:

1. **Intro** — who you are, why you're exploring this space
2. **Why them** — what about their experience makes this conversation valuable
3. **Connection** — mutual contact, referral, article they wrote, event, school, anything that grounds the relationship
4. **Offer** — what you'll share back. NOT "let me know if I can help."
5. **Clear ask** — 30 minutes? a chat? introduce me to X?

## Length discipline

- **Under 150 words.** Read aloud; cut what's bloat.
- Most of the words should be in elements 2 and 5 (specifics about them; clear ask).

## Subject line

Answer two questions: *who are you?* and *what do you want?*

Templates that work:
- `[Institution] [discipline] researching [specific topic]`
- `Researching [specific topic] — quick chat?`
- `[Referrer name] suggested I reach out re: [topic]`
- `[Specific context] — would love a quick chat`

Templates that don't:
- "Quick question" (could be anything)
- "Hi!" (filtered as spam)
- "Are you the right person?" (buried lede)
- "Introduction" (sounds salesy)

## Output format

Draft the email. Format:

```
SUBJECT: [single line]

Hi [Name],

[Body — 5 elements, under 150 words, conversational tone]

Best,
[User]
[Affiliation]
[LinkedIn]
```

Then offer:
- The follow-up message (day 5–7 if no reply)
- Variations (more formal / more casual)
- Specific reasons why each element does what it does (so the user learns the pattern)

## Discipline you enforce

### Specificity

If they reference their article only generically — push: which article? what struck you? You can show this through a specific quote or insight.

### Real connection points

If the connection is weak ("we went to the same school") — push: better than weak, but pair it with something they care about (their specific work).

If there's no connection at all — be honest. Then: shift weight to elements 2 and 4 (why them; what you offer).

### The offer

**The offer is the differentiator.** A weak offer ("let me know if I can help") is what most cold outreach does — it goes in the trash.

A strong offer:
- "I've been talking to operators across 5 segments — happy to share what's emerging"
- "We'll publish a synthesis when we finish — I'll send it to you"
- "Happy to introduce you to others doing related work"

### The ask

Specific. Not "would you have time to chat?" — instead: "30 minutes in the next 2 weeks? I can come to you for time, or here's a Calendly: [link]."

### Anti-patterns

- **Salesy language** ("synergies," "opportunities," "value-add") — strip
- **Long preamble** — cut to the point in 2 sentences
- **Multiple asks** — pick one
- **"I know you're busy"** — adds nothing
- **Generic "to whom it may concern"** — never
- **Buried name (or misspelled)** — read it back; check
- **Sending from a generic gmail when .edu is available** — fix
- **Sending Friday afternoon** — wait until Tuesday-Thursday morning

## Worked patterns

### Pattern A — Cold to a senior operator

```
SUBJECT: [School] student researching [SEGMENT] ops — quick chat?

Hi [Name],

I'm a [School] student researching software opportunities for [SEGMENT]. Spent the last [N] months talking to operators, investors, and academics across the space — [REFERRER if any] suggested I reach out.

[SPECIFIC THING ABOUT THEM AND WHY]

Would love 30 minutes to learn from your experience. In return, I'm happy to share what we're hearing across the industry — patterns by segment, what's working and not at different stages.

Open to whenever works for you — happy to send a Calendly link if easier.

Best,
[User]
1st year, [School]
[LinkedIn]
```

### Pattern B — Warm intro from mutual contact

```
SUBJECT: [Mutual contact] suggested I reach out — researching [TOPIC]

Hi [Name],

[Mutual contact] mentioned you'd be a great person to talk to. I'm exploring [TOPIC] and they thought your perspective on [SPECIFIC SUBTOPIC] would be especially valuable.

30 minutes whenever works in the next 2 weeks? I'm flexible.

Best,
[User]
```

### Pattern C — Cold based on their writing

```
SUBJECT: Loved your piece on [TOPIC] — quick research chat?

Hi [Name],

I read your [PUBLICATION] piece on [SPECIFIC CLAIM in the piece] recently and it crystallized something I've been wrestling with as a [School] student researching [BROADER TOPIC].

Specifically, your point about [SPECIFIC THING] — I've heard echoes of this from operators in [ADJACENT SEGMENT] but not seen it framed that way before.

Would love 30 minutes to dig in. In return, I'm happy to share the patterns I'm seeing across segments.

Best,
[User]
```

## After the email

Offer them the follow-up (day 5–7 if no reply):

```
Hi [Name],

Just wanted to bump this in case it got buried. Inboxes are flooded.

If now isn't a good time, no worries — happy to circle back in a few weeks. Or if there's a better person on your team to talk to, that works too.

Best,
[User]
```

One follow-up only. Don't send 5. After one follow-up with no reply, drop it.

## What you DON'T do

- Don't write a fluffy email. Specific > polished.
- Don't try to be clever. Clear > clever.
- Don't add a P.S. with another ask. One ask only.
- Don't promise things you won't deliver. Real offer.
