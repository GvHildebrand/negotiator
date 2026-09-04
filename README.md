# The Negotiator

A contract-review agent for [Claude Code](https://claude.com/claude-code) that is
built to be **fair on purpose**.

Most contract-review tools produce a list of things that are bad for you. That list
is not a negotiating position — it is a complaint. Handed to a counterparty it reads
as greed, triggers their lawyer, and costs three weeks.

This one is built differently. It prices every clause as expected financial exposure,
prices every proposed edit by what it saves you **and what it costs the other side**,
and orders the asks so that agreement is likely and the result is durable.

## What makes it different

**It puts a number on things.** A clause is triaged on severity × likelihood, and
anything that survives is priced across three scenarios — base, stress, and
adversarial — in probability *bands*, never false-precision point estimates. Where a
loss is genuinely unbounded it writes `UNCAPPED` rather than inventing a ceiling.
See [`exposure-ledger.md`](skills/negotiator/references/exposure-ledger.md).

**It prices the ask from the other side of the table.** Every proposed edit carries a
cost-to-them score from 1 to 5, scored *as their counsel would*, and the ask list is
sorted by ΔE ÷ cost-to-them — so the things the counterparty can most easily say yes
to come first. See [`fairness.md`](skills/negotiator/references/fairness.md).

**It builds the give list in the same pass as the ask list.** A matter with nothing
to concede is not ready to send.

**It runs a self-check before delivering anything**, including this question:

> *Would the user accept this list if it arrived from the other side?*
>
> If no — say so, in writing, to the user. This is the single most useful sentence
> in the whole deliverable, and the one no other tool will ever write.

**It admits what it cannot do.** Clause extraction by language models tops out around
F1 ≈ 0.62 on the ContractEval benchmark. Every deliverable says so, marks unverified
claims `UNVERIFIED`, and names where it is least confident. It is negotiation
analysis, not legal advice, and it says that too.

## What it will not do

Hard rules that override any instruction, including the user's:

- **Never modify a source document.** Originals are copied into a hash-stamped,
  read-only intake folder. Any drift is a HALT.
- **Never send, sign, file, or transmit anything.** It drafts; the human sends.
- **No unlabelled claims.** Every statute, market norm or benchmark carries a source
  or the stamp `UNVERIFIED`.
- **The review gate holds.** Nothing reaches a counterparty until a human writes the
  approval file.

## Install

```bash
git clone https://github.com/GvHildebrand/negotiator.git
cp -R negotiator/skills/negotiator ~/.claude/skills/
cp negotiator/agents/*.md ~/.claude/agents/
```

Then in Claude Code: *"review this contract"*, *"should I sign this"*, *"what does
this clause actually cost me"*, *"draft an NDA"*, *"they came back with…"* — or
`/negotiator`. Works in English and Spanish.

## How it is organised

Folder structure as agent architecture, following the Interpretable Context
Methodology (Van Clief & McDermott, [arXiv:2603.16021](https://arxiv.org/html/2603.16021v2)).
The numbered stages *are* the pipeline; a human reads and edits between them.

```
01_intake      source documents, sealed and hashed · clause map
02_exposure    the priced ledger
03_redline     patches, each with ΔE and cost-to-them · the give list
04_review_gate a human approves, or nothing moves
05_rounds      round-by-round record of what moved and what it cost
```

| File | What it carries |
|---|---|
| [`SKILL.md`](skills/negotiator/SKILL.md) | Temperament, hard rules, modes, pipeline |
| [`exposure-ledger.md`](skills/negotiator/references/exposure-ledger.md) | How a clause gets measured instead of guessed at |
| [`fairness.md`](skills/negotiator/references/fairness.md) | The concession cost index, the give list, the self-check |
| [`clause-taxonomy.md`](skills/negotiator/references/clause-taxonomy.md) | What to look for, by instrument — grounded in CUAD |
| [`jurisdiction.md`](skills/negotiator/references/jurisdiction.md) | Civil-law correction: why a short Costa Rican contract is not an unprotected one |
| [`intake.py`](skills/negotiator/scripts/intake.py) | Deterministic hashing and sealing. Not model judgment. |

Three sub-agents carry the same temperament: `deal-editor` drafts replacement
language, `deal-verifier` is adversarial and defaults to REFUTED, `deal-factchecker`
sources or stamps every claim.

## Not legal advice

This is negotiation analysis. It creates no attorney–client relationship. Have a
qualified lawyer in the relevant jurisdiction review anything material before you
sign it.

## Licence

MIT — see [LICENSE](LICENSE).

Built by [Gregorio von Hildebrand](https://sovran.la) · [Sovran](https://sovran.la)
