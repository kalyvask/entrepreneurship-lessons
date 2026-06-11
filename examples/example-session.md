# What a session feels like

> **Illustrative transcript.** Authored for documentation to show the shape of a first session —
> not a live capture. The venture, people, and numbers are invented. The behaviour shown (interview
> over form-filling, evidence-gated scores, write-back and read-back) is the contract every state
> skill follows; see `scaffold/README.md`.

The founder has cloned the repo, copied `scaffold/` into their venture folder, opened Claude Code,
and typed `/ent-intake`.

---

**Founder:** Set me up. I'm building RotaCover — a shift-cover marketplace for independent gyms.
I've done the discovery, the concept's solid, I'm ready to scope the MVP. Put me at the build stage.

**Coach:** Before I place you anywhere, three quick ones. What's the most pressing question you're
trying to answer this week?

**Founder:** Honestly — what to build first.

**Coach:** And what evidence do you have today? Conversations, commitments, anything someone *did*
rather than said?

**Founder:** Nine interviews with gym owners. Almost all of them said no-show coverage is a
nightmare and they'd love something like this.

**Coach:** "Said" is where I have to slow you down. Walk me through the last interview — after the
call, what did that owner *do*? Did anyone send you their rota, intro you to another owner, ask to
pay, or show you a workaround they'd already built?

**Founder:** One of them — Dana, she runs two sites — showed me a WhatsApp group she set up with
freelance instructors from three other gyms. They cover each other's no-shows informally. The
others were more "yeah, that sounds great."

**Coach:** That WhatsApp group is the only desperation signal in what you've told me — one real
workaround, built independently. That's a 2 on workaround evidence, not a 3 (one observed, not
multiple). On desperation markers across the nine: one person with behaviour, eight with
compliments — that's a 1. Who exactly is the *who*? Can you name ten real gyms that look like
Dana's?

**Founder:** Not ten. Maybe three or four multi-site independents like hers.

**Coach:** Then here's where I'm placing you, and why:

> **Stage 02 — Customer Discovery**, not Stage 05.
> You have an insight and one genuinely desperate-looking customer, which is exactly what Stage 02
> exists to multiply. Scores I'm recording for the Stage 02 gate: **narrow who 1** (a segment, not
> ten nameable gyms), **desperation markers 1** (one of nine with behaviour), **workaround evidence
> 2** (Dana's WhatsApp group — observed, real), **recurrence 2** (no-shows came up unprompted in
> most calls), **Mom Test discipline 1** (eight of nine answers were compliments, which usually
> means pitching), **sample depth 1** (nine interviews).
> Blockers: can't name 10 in the narrow who; desperation unproven outside one account.
> Leap of faith, as I heard it: *multi-site independent gym owners will pay to fill a no-show from
> a vetted pool instead of running it through a free WhatsApp group.*
> Did I get this right — and is there anywhere I was too generous?

**Founder:** I'd say desperation is at least a 2 — they were all really enthusiastic.

**Coach:** Enthusiasm is the thing this library refuses to count. A 2 needs behaviour from several
people — pre-pays, workarounds, unprompted urgency. You have behaviour from one. If two more owners
show me a workaround or put money down, it's a 2 and I'll update the file the moment you tell me.
It stays a 1 today.

**Founder:** Fine. What do I do next?

**Coach:** One thing: ten more interviews, but only with multi-site independents like Dana — the
narrow who that showed behaviour. Use `/ent-interview-prep` before each. The thing *not* to do
right now: scope the MVP. Building for eight polite gyms is the classic way to spend three months
learning nothing.

I've written the workspace. `founder-state.yaml` now reads:

```yaml
venture: "RotaCover"
one_liner: "Shift-cover marketplace that fills gym no-shows from a vetted instructor pool, for multi-site independent gyms."
updated: "2026-06-01"
stage:
  current: "stage-02-customer-discovery"
  entered: "2026-06-01"
  gate_scores:
    narrow_who: 1            # a segment, not 10 nameable gyms
    desperation_markers: 1   # 1 of 9 with behaviour (interviews.csv row 7)
    workaround_evidence: 2   # Dana's cross-gym WhatsApp pool, observed (interviews.csv row 7)
    recurrence: 2            # no-shows raised unprompted in most calls
    mom_test_discipline: 1   # compliment-heavy answers; likely pitching
    sample_depth: 1          # 9 interviews
leap_of_faith: "Multi-site independent gym owners will pay to fill a no-show from a vetted pool instead of running it through a free WhatsApp group."
narrow_who: "Multi-site independent gyms (2-5 sites) whose owners already coordinate freelance cover informally; can name 4, need 10."
blockers:
  - "Cannot yet name 10 gyms in the narrow who."
  - "Desperation shown by 1 of 9 interviewees; behaviour unproven across the segment."
history:
  - { date: "2026-06-01", from: "", to: "stage-02-customer-discovery", why: "Intake. Insight real; one workaround observed (Dana); evidence too thin for Stage 03+. Founder arrived asking to build." }
```

…and your nine interviews are in `interviews.csv`, scored on the four desperation markers, with
Dana's workaround flagged. Next session, just open Claude Code and talk — `/ent-stage-router` reads
this file and picks up exactly here.

---

## What to notice

- **The founder asked for Stage 05 and got Stage 02** — placement followed the evidence, not the
  request, and the read-back said which dimension was generous and why.
- **A score-up request was refused** without new behaviour — and the coach said precisely what
  would earn the upgrade.
- **The founder never touched a file.** The interview produced the state; the YAML above was
  written, then read back in plain English for confirmation.
- **The routing was one step**, with the most important thing *not* to do named out loud.
