# Verification-First Diligence

A working method for pressure-testing a set of factual claims before money, reputation, or a
decision rides on them. It runs in two directions:

- **Outbound (founder self-diligence).** Before your PMF memo, your primer, or your pitch meets a
  sharp reader, treat your own claims the way an investor will. Anything in the document that dies
  on first contact with scrutiny costs you more than the gap itself would have.
- **Inbound (evaluating someone else).** Diligencing a company, a deal, or a partner's claims —
  the discipline that feeds the investment-style memo in your `thesis_ledger.md`.

AI makes this fast; it does not make it true. The whole method is built around one rule: **treat
every AI output as a hypothesis, never as a fact.**

## The core move — verify, flag, or discard

Every claim in the set gets exactly one of three treatments:

| Treatment | When | What you do |
|---|---|---|
| **Verify** | A primary source exists | Find it; record the source next to the claim |
| **Flag** | No primary source found | Mark it unverified, note the gap, carry it as a question |
| **Discard** | Can't be sourced and isn't load-bearing | Drop it from the document or the model |

Nothing gets copied forward as fact without a source or a caveat. A claim with a confident tone
and no trail is the most dangerous object in a diligence file.

## Claim-by-claim targets, not open-ended research

"Research this company" produces a summary of the company's own materials — no verification, no
edge. The productive shape is a list of **specific claims with a required status per claim**:

- Enumerate the load-bearing claims (team backgrounds, funding amounts and their actual structure,
  market numbers, named partnerships, production or traction figures).
- For each, require: what was found, the source (ask for the URL — the request itself catches
  fabricated citations), and a status: verified / partially verified / unverified.
- Work section by section rather than in one giant pass — long single passes degrade in quality
  exactly where you stop reading carefully.
- Make vague claims concrete before verifying them. "$1.4B of government backing" is not a fact
  until you know whether it is a grant, a loan, a tax credit, or a press release about intent —
  and whether any of it has been disbursed.

Tell the assistant explicitly that you will fact-check independently, so accuracy beats
impressiveness. Ask it to rate its own confidence and to say plainly when it cannot confirm
something — an honest "unverified" is worth more than a fluent guess.

## The what-must-be-true frame

Verification tells you what is; this tells you what has to be. For the decision at hand (the
investment returns 3x; the memo's verdict holds; the partnership is worth it), lay out the
assumptions by category — market, execution, competitive, team — and rate each on three axes:

- **Likelihood** — high / medium / low, given what you verified.
- **Verifiability** — can this be known *before* the decision, and how (data room, management
  call, expert network, a behavioural test)?
- **Impact if wrong** — deal-breaker / significant / minor.

Low-verifiability + deal-breaker assumptions are where the remaining diligence time goes. This is
`frameworks/judgment_and_pareto.md` applied to diligence: verify the claims that carry the
valuation, not everything equally.

## Iterate in rounds

Diligence is never one pass. The rounds, in order:

1. **Landscape** — get oriented; collect the claim set.
2. **Verify** — the verify/flag/discard pass, claim by claim.
3. **Gaps** — list what still matters but couldn't be confirmed: why it matters, how to fill it,
   and what you'll assume if it can't be filled.
4. **Decision frame** — the what-must-be-true table; convert research into criteria.
5. **Bear case** — assistants agree by default, so adversarial pressure must be explicit. Run
   `/ent-red-team` on the surviving thesis: the most likely path to zero, what you're
   under-weighting, the questions that would make the principals uncomfortable, why informed
   people pass.

## A note on numbers

AI is good at *structuring* a model — which rows and columns should exist, which assumptions to
challenge, how scenarios compare — and unreliable at arithmetic. Use it to build the skeleton,
pressure-test an assumption ("do we actually need this line item?"), and run
conservative/base/optimistic scenarios; own the math yourself. Same discipline as
`frameworks/unit_economics.md`: the envelope is for catching a broken structure, not for
predicting the P&L.

## The founder direction, concretely

Before sharing a PMF memo or walking into a diligence process, run the inbound method on
yourself:

- Every factual claim in the memo (market numbers, "the only ones who…", traction, retention)
  gets the verify/flag/discard pass — with the workspace artifact cited where one exists
  (`pmf_dashboard.md`, `experiment_log.md`, `interviews.csv`).
- Flags don't get polished away; they get labelled as open. An honest "unverified, here's how
  we'll know" reads stronger than a confident claim that collapses under one question.
- One caution: for PMF claims specifically, documents never outrank behaviour. A verified market
  report does not substitute for a desperate customer; this method checks your *facts*, the
  validation sequence checks your *bet*.

## Where this lives in the journey

- `/ent-diligence` — runs this playbook end to end
- `/ent-red-team` — round 5; adversarial reasoning on whatever survives verification
- `/ent-pmf-memo` — apply the founder direction before the memo is shared
- `/ent-thesis` — the inbound direction feeds the investment-style memo in `thesis_ledger.md`
- `frameworks/judgment_and_pareto.md` — verify what carries the decision, not everything
- `frameworks/ai_lifecycle.md` — the verification mindset for AI-assisted work generally

## Source

Synthesized in this repo's own words from Diego Oppenheimer's GSB Applied-AI session on AI for
startup investing (verification-first research, the what-must-be-true frame, iteration rounds,
the bear-case discipline). See `SOURCES.md`.
