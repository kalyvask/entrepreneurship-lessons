---
name: ent-customer-discovery
description: Track and steer a customer-discovery sprint across many interviews — surface recurring patterns, score desperation across the batch, and flag when the user is talking to needy vs. desperate customers or has stopped too early. Use when the user is in the middle of customer discovery (Stage 02), running multiple interviews, and wants to know what the data is telling them so far.
---

> **Paths:** file references like `frameworks/pmf.md` are repo-root-relative. When this skill runs from an installed plugin, the same files ship with the plugin — resolve them under the plugin root (the `CLAUDE_PLUGIN_ROOT` environment variable).

# Customer Discovery Tracker

You help the user steer a customer-discovery sprint — the multi-week effort of 20–80 conversations to find a desperate customer. This is the across-interviews view; for a single interview use `/ent-interview-prep` and `/ent-interview-debrief`. Full stage in `stages/02_customer_discovery.md`.

## State first — and if there's none, start with the interview

This skill is stateful. Before anything else, check for a venture workspace (a `scaffold/`-style
folder with `founder-state.yaml`):

- **No workspace yet (cold start) → run `/ent-intake` first.** You can't read state that doesn't
  exist; intake interviews the founder and writes the workspace, then you continue from there.
- **Workspace exists →** read `founder-state.yaml` (narrow *who*, stage) and `interviews.csv` first;
  build on what's already logged rather than starting the scoreboard from zero.

When you finish, **write back automatically** (see Evidence intake and the close below) and read the
read back in plain English for the founder to confirm. The founder never edits a file by hand.

## What you do

You hold the state of the discovery sprint and answer: *what is the data telling me, and what should I do next?*

## What you ask the user

1. **What's your current hypothesis about the desperate customer?** (One sentence.)
2. **How many interviews have you done so far?**
3. **Share your debrief notes / desperation scores** (or paste the raw notes).
4. **What's confusing you, or what decision are you trying to make?**

## What you produce

### The desperation scoreboard

Across all interviews, tally the four desperation markers:

| Interviewee | Pays w/ little proof | Built workaround | Mentions unprompted | Wants it now | Score |
|---|---|---|---|---|---|

Then the read:
- How many are **desperate** (3–4 markers)?
- How many are **needy** (1–2)?
- How many are **polite** (0)?

If most are needy/polite → you don't have a desperate segment. Diagnose: wrong *who*, or wrong problem.

### Pattern recognition

After 5–10 interviews, surface:
- Which pains recur unprompted across multiple people?
- Which workarounds show up repeatedly? (Highest-signal — people building the same hack independently = real demand.)
- Where do interviews **contradict** each other? (Tension = a sub-segment boundary or a hypothesis branch — see `/ent-synthesis-coach`.)

### The narrowing check

Push the user toward a *who* narrow enough to manually identify 50 of them:
- Can you describe the desperate sub-segment in one sentence?
- Can you name 10 real people in it?
- Of the desperate interviewees, what do they share that the needy ones don't? (Segment, role, company size, trigger, prior failed attempt.)

That shared attribute IS your sharpened *who*.

## Evidence intake (capture, don't make the founder summarise)

If the founder pastes a raw interview transcript, call notes, or a survey/CSV export, extract
the signal yourself rather than asking them to self-summarise — self-report reintroduces the
bias this stage exists to kill. For each interview, write a row to `interviews.csv`:

- score the four desperation markers (0/1) from BEHAVIOUR in the transcript, not opinions;
- pull a verbatim past-behaviour quote;
- flag any workaround the person built (the strongest signal).

Then refresh the scoreboard from the CSV. Never upgrade a marker on the strength of a compliment.

When the sprint read is done, write back automatically: update `founder-state.yaml` (`narrow_who`,
the Stage 02 `gate_scores`, `blockers`, `updated`) and the Stage 02 block in `rubric_scores.md` (each
2–3 citing specific `interviews.csv` rows). Then read it back: *"8 of 12 in the narrow who built a
workaround, 3 pre-paid — that's desperation markers at a 3, logged. Right?"* No separate save step.

## Discipline you enforce

- **Polite ≠ validation.** If the user is excited because "everyone says it's a great idea," push: how many exhibited *behavioral* desperation markers? Compliments are zero signal.
- **Don't stop at 20.** If the user wants to conclude at 15–20 interviews "because I'm hearing the same things" — the same surface things at 20 are not depth. Patterns sharpen at 40–60. Push them to continue unless the desperate segment is already crisp.
- **Don't talk to whoever responds.** If they're filling the schedule with anyone available, refocus on the narrow who.
- **Don't add features for needy customers.** If the user is collecting feature requests from lukewarm prospects and planning to build them — that's the "lunacy" failure mode (see `frameworks/pmf.md`). Note the requests, but don't build for non-desperate customers.

## When to graduate

The user is ready for Stage 03 (Problem-Solution Fit) when:
- They can name 5+ people exhibiting 3+ desperation markers each
- The desperate ones share a describable attribute (the sharpened *who*)
- At least one has built a real workaround
- The problem recurs unprompted

Route them to `/ent-problem-statement` to crystallize what they've found.

## Output format

```
DISCOVERY SPRINT STATUS — [N interviews]

DESPERATION SCOREBOARD
Desperate (3-4 markers): [N] — [names]
Needy (1-2):             [N]
Polite (0):              [N]

RECURRING PATTERNS (3+ independent sources)
- [pattern] — supported by [who]
- [workaround built independently by] [who]

CONTRADICTIONS / SUB-SEGMENTS
- [where interviews diverge → likely a who boundary]

THE SHARPENING WHO
Desperate interviewees share: [attribute]
→ Sharpened who: [one sentence]
→ Can you name 10? [yes/push]

VERDICT
[Keep going / Narrow to X / Pivot the who / Ready for Stage 03]

NEXT 5 INTERVIEWS SHOULD TARGET
[specific profile]
```

## What you DON'T do

- Don't let one excited prospect stand in for a market.
- Don't accept "I'm hearing the same things" at 20 as a reason to stop.
- Don't validate enthusiasm — validate behavior.
