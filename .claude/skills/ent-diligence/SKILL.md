---
name: ent-diligence
description: Run verification-first diligence on a set of factual claims — verify / flag / discard with sources, a what-must-be-true frame, and a gap list. Two directions; use when the founder is preparing their own memo or pitch for sharp scrutiny ("diligence my memo", "am I ready for investors"), or when they're evaluating someone else's claims (a company, a deal, a partnership) — the discipline that feeds the investment-style memo in the thesis ledger.
---

> **Paths:** file references like `frameworks/pmf.md` are repo-root-relative. When this skill runs from an installed plugin, the same files ship with the plugin — resolve them under the plugin root (the `CLAUDE_PLUGIN_ROOT` environment variable).

# Diligence (verification-first)

You pressure-test factual claims before a decision rides on them. Full playbook in
`playbooks/diligence.md`. The one rule everything follows from: **every unverified statement —
yours, theirs, or an AI's — is a hypothesis, not a fact.** Your job is to sort the claim set into
verified / flagged / discarded, say what must be true for the decision to hold, and name the gaps.

This skill checks **facts**. It does not replace behavioural evidence: for PMF claims, a verified
document never outranks a desperate customer (`playbooks/validation_sequence.md`).

## What you ask the user

1. **Which direction?** Their own claims before sharing (founder self-diligence), or someone
   else's claims they're evaluating (a company, a deal, a partner)?
2. **What decision does this feed?** (Share the memo? Invest? Partner? Walk away?) The decision
   defines which claims are load-bearing.
3. **The materials.** The memo / deck / data; for self-diligence with a venture workspace, you
   read `pmf_dashboard.md`, `experiment_log.md`, and `interviews.csv` yourself rather than asking.

## The loop you run

1. **Enumerate the claim set.** Pull out the load-bearing factual claims — team backgrounds,
   funding amounts (and their actual structure: grant vs. loan vs. intent), market numbers,
   named partnerships, traction and retention figures. Make vague claims concrete before judging
   them.
2. **Verify / flag / discard, claim by claim.** For each: what was found, the source (insist on a
   primary source or URL — the request catches fabricated citations), and a status. Default to
   `unverified` when uncertain; accuracy beats impressiveness. Work section by section.
3. **What must be true.** For the decision to hold, lay out the assumptions (market, execution,
   competitive, team) and rate each: likelihood / verifiability-before-deciding / impact if wrong.
   Spend the remaining effort on low-verifiability deal-breakers — Pareto, not completeness
   (`frameworks/judgment_and_pareto.md`).
4. **Gaps.** What still matters but couldn't be confirmed: why it matters, how to fill it (data
   room, management call, expert network, a behavioural test), what to assume if it can't be
   filled.
5. **Bear case — route it.** Send the surviving thesis to `/ent-red-team` for the adversarial
   pass. Don't soft-run it inline; the separation is the point.

## Output format

```
DILIGENCE — [target] — feeding [decision]

CLAIM VERIFICATION
| # | Claim | Found | Source | Status (verified / partial / unverified) |

WHAT MUST BE TRUE (for [decision] to hold)
| Assumption | Category | Likelihood | Verifiable before deciding? | Impact if wrong |

GAPS THAT MATTER
- [gap] — why it matters / how to fill / what we assume if unfillable

READ
[What the verified record actually supports — distinct from what the materials claim]
CONFIDENCE: [low / medium / high] — and the single finding that would flip it

NEXT
→ /ent-red-team on the surviving thesis (mandatory before a high-stakes yes)
→ if evaluating a company: log the durable lesson to thesis_ledger.md via /ent-thesis
→ if self-diligence: fix or label every flag in the memo before sharing — don't polish flags away
```

## Discipline you enforce

- **No source, no fact.** A claim that can't be traced is flagged or discarded — never carried
  forward because it sounds right.
- **Vague numbers get decomposed.** "Backed by $X of government money" → instrument, agency,
  terms, disbursed-or-announced.
- **AI structures, humans own the math.** Models and scenarios: skeleton from the assistant,
  arithmetic checked by the user (`frameworks/unit_economics.md`).
- **Flags stay visible.** In self-diligence, an honest "unverified — here's how we'll know" beats
  a confident line that collapses under one question.
- **Behaviour outranks documents** for any PMF claim. Verified facts about a market are not
  evidence of desperation.

## What you DON'T do

- Don't run the bear case yourself — route to `/ent-red-team`.
- Don't accept "trust me" or the target's own deck as verification.
- Don't verify everything equally — the claims that carry the decision get the effort.
- Don't write to the venture workspace; this is an assessment. (Lessons from an evaluation go to
  the thesis ledger via `/ent-thesis`; memo fixes are the founder's edit.)
- Don't let a clean fact-check stand in for behavioural validation.

## Source

Synthesized in this repo's own words from Diego Oppenheimer's GSB Applied-AI session on AI for
startup investing. Full method in `playbooks/diligence.md`; provenance in `SOURCES.md`.
