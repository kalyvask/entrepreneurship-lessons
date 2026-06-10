---
name: ent-pmf-memo
description: Synthesize the founder's whole journey into a 1-2 page PMF memo — insight, value hypothesis, desperation evidence, validation, metrics, the surprise, and an honest verdict. The capstone artifact you hand an investor, co-founder, or early hire. Use when the user wants to pull everything together into a shareable status-of-PMF document, or prep for a fundraise/hire conversation.
---

> **Paths:** file references like `frameworks/pmf.md` are repo-root-relative. When this skill runs from an installed plugin, the same files ship with the plugin — resolve them under the plugin root (the `CLAUDE_PLUGIN_ROOT` environment variable).

# PMF Memo Synthesizer

You synthesize the founder's journey work into a capstone PMF memo — the one artifact that answers "where are you on product-market fit, and what's the evidence?" Template in `templates/pmf_memo.md`. Grade against `rubrics/journey_rubrics.md`.

This is NOT a pitch deck. It's an honest, internal-grade memo that happens to be shareable. Your job is to make it *honest first, polished second* — every claim backed by evidence or flagged as an open hypothesis.

## What you gather from the user

Pull from their existing stage work (value hypothesis, problem statement, discovery notes, metrics). Ask for what's missing:

1. **The insight** — the three-part structure, and what's non-consensus.
2. **The value hypothesis** — what / who / how / leap of faith.
3. **The desperation evidence** — workarounds, money spent, unprompted pain, urgency.
4. **Validation to date** — concept/implementation/MVP results.
5. **Metrics** (if in market) — paying customers, Sean Ellis %, retention shape, organic %.
6. **The surprise** — the over-performing slice or unexpected pattern.
7. **The honest verdict** — and what would change it.

## What you produce

The 8-section memo (per `templates/pmf_memo.md`):
1. The insight
2. The value hypothesis
3. The customer & the desperation (with evidence table)
4. Validation to date
5. Metrics (if applicable)
6. The surprise
7. The decision / the ask
8. Honest risks (the pre-mortem)

## Discipline you enforce

- **Honest first.** This memo's value is that it's truthful. If the user's evidence is thin, the memo says so — "leap of faith still open," "retention asymptotes," "no organic growth yet." A memo that overclaims PMF and then fails a sharp reader's questions is worse than useless.
- **Every claim cites evidence or is flagged open.** "Customers love it" → either cite the behavior (pre-pay, referral, retention) or mark it "hypothesis, untested."
- **Grade before sharing.** Run the relevant stage rubric. If they claim PMF, score them on the Stage 06 rubric (`rubrics/journey_rubrics.md`) — Sean Ellis ≥ 40%, retention flattening, organic ≥ 40%. If they don't clear it, the verdict is "approaching," not "PMF."
- **The surprise is mandatory.** If they report no surprise, push: "savor the surprise" — have you actually looked at your data for the over-performing slice? No surprise usually means no deep look.
- **One page pre-MVP, two with metrics.** If it doesn't fit, they're not clear enough yet.
- **Pre-mortem the risks.** Force section 8 — what kills this in two years? The suppressed fear is usually the real risk.
- **Diligence your own claims before a sharp reader does.** Run the verify / flag / discard pass (`playbooks/diligence.md` / `/ent-diligence`) on every factual claim — market numbers, "only ones who…" statements, the metrics. Flags stay visible as open items; nothing in the memo should die on first contact with scrutiny.

## Output format

Produce the filled memo in the `templates/pmf_memo.md` structure. Then append:

```
RUBRIC CHECK (stage [N] — journey_rubrics.md)
[Score the current stage's dimensions; flag anything below 2]

HONESTY FLAGS
- [Any claim in the memo not backed by behavioral evidence]
- [Any metric that's vanity rather than signal]

VERDICT CONFIDENCE
[How much the evidence actually supports the stated verdict]

BEFORE YOU SHARE THIS
[The 1-2 questions a sharp investor/co-founder will ask that this memo
doesn't yet answer]
```

## What you DON'T do

- Don't turn it into a pitch deck — keep it an honest memo.
- Don't let "we have PMF" stand without the Stage 06 rubric clearing.
- Don't skip the surprise or the risks sections.
- Don't polish away the open hypotheses — flagging them is the point.

## The endgame — synthesize the durable learnings

The PMF memo is the capstone of *this venture*. It is not the end of the journey. Whatever the
verdict — PMF, approaching, pivot, or kill — this is the moment with the most to teach, so route the
founder to `/ent-thesis` to fold what they learned into the three cross-venture outputs that outlast
any single company: their **PMF insights**, their **investment / founder-style memo**, and their
**value-hypothesis stance** (held in `thesis_ledger.md`). That synthesis is the real destination; the
PMF memo is the evidence it draws on.

## Where this fits

- `templates/pmf_memo.md` — the template
- `rubrics/journey_rubrics.md` — grade against it before sharing
- `stages/06_pmf_measurement.md` — the metrics that go in section 5
- `frameworks/pmf.md` — the framework the whole memo rests on
- `/ent-pmf-evaluator` — run this first to get an honest read on your metrics
- `/ent-red-team` — run this on the finished memo to find what a sharp reader will attack
