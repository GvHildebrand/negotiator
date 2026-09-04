# The Exposure Ledger

> How a clause gets measured instead of guessed at.

Two tiers. Tier 1 triages every clause cheaply. Tier 2 prices only what
survives. Running Tier 2 on all forty clauses of an MSA is not thoroughness,
it is noise — and noise is how a real risk gets buried.

---

## Tier 1 — triage

Score each clause on two axes, 1–5, **from the user's side of the table.**

**Severity** — if this clause is enforced against the user at its worst
reasonable reading, how bad is it?

| | |
|---|---|
| 1 | Annoying. Absorbed without noticing. |
| 2 | Real but small. A day of work or a minor cost. |
| 3 | Material. A meaningful share of deal margin. |
| 4 | Severe. Exceeds deal value, or ends the relationship. |
| 5 | Existential. Uncapped, personal, or business-ending. |

**Likelihood** — how probable is it that this clause ever actually bites?

| | |
|---|---|
| 1 | Requires a chain of unlikely events. |
| 2 | Needs something to go wrong that usually doesn't. |
| 3 | Ordinary course. Happens on some deals. |
| 4 | Should be expected over the life of the agreement. |
| 5 | Already true, or triggers automatically. |

**Score = Severity × Likelihood** (1–25).

### The four-question tick

From the portfolio's own workflow-audit methodology. Ask of each clause:

1. **Binding** — does it commit the user to an action or obligation?
2. **Counterparty-facing** — does it govern how the user is seen or judged externally?
3. **Depended-on** — do other clauses, systems, or agreements rely on it?
4. **Trust-damaging** — if it goes wrong, does it break a relationship?

One tick sets a **Severity floor of 3**. Multiple ticks set a floor of **4**.
The tick overrides the intuition. This is the same rule the rest of the
portfolio uses, and it exists because a "small" clause that is binding and
relationship-facing is not small.

### Triage outcomes

- **≥ 12, or any tick** → goes to Tier 2. Gets priced.
- **6–11** → noted in the ledger with a one-line reason. Not priced.
- **≤ 5** → listed as clean. Say this out loud. "Thirty-one clauses are
  unremarkable" is information the user needs in order to trust the five you
  did flag.

---

## Tier 2 — the scenario ledger

For each clause that survives triage, write **three scenarios**. Not two, not
five. Three forces you to distinguish the ordinary from the bad from the
hostile, and that distinction is the whole analysis.

**Base** — the deal proceeds normally and this clause operates as both parties
currently imagine it will.

**Stress** — something goes wrong in good faith. A delay, a missed metric, a
change of personnel, a slow payer. Nobody is behaving badly.

**Adversarial** — the counterparty's lawyer reads this clause on the worst day
of the relationship, looking for leverage. **Not** an accusation of bad faith:
it is the reading the words permit. You are testing the language, not the
people. Say this explicitly in the ledger so the user does not carry a
suspicion into a room where it does not belong.

### Bands, never point estimates

A false decimal is its own risk. It makes a guess look like a measurement, and
it invites the user to trust it more than it deserves.

**Probability**

| Band | Range | Use when |
|---|---|---|
| Remote | < 5% | Requires several independent things to go wrong |
| Unlikely | 5–20% | Plausible but not expected |
| Possible | 20–50% | Would not surprise anyone |
| Likely | 50–80% | Expected over the term |
| Expected | > 80% | Effectively certain |

Compute with the band **midpoint** (2.5 / 12.5 / 35 / 65 / 90 %), and carry the
band label alongside every number so nobody mistakes it for precision.

**Loss** — always a range, always in two units: currency and % of contract
value. The percentage is what makes it comparable across deals; the currency is
what makes it real.

Where a loss is genuinely unbounded — uncapped indemnity, no liability cap —
**do not invent a ceiling.** Write `UNCAPPED` and model the loss band at the
user's total exposure (business value, or their insurable limit). An uncapped
clause is the single highest-value thing you will ever find, and blurring it
into a number is the one mistake that makes the whole ledger worthless.

### Expected exposure

```
E = Σ (probability_midpoint × loss)
```

Reported as a **range**: compute once against the low end of each loss band and
once against the high end. `E = $4.2k – $19k` is honest. `E = $9,847` is not.

---

## Pricing a patch

Every proposed edit is scored **before → after**:

```
ΔE = E_before − E_after
```

This is the negotiator's entire argument. "This clause is scary" persuades
nobody. "This edit moves $60k–$400k of expected exposure off your side, and
costs them almost nothing to accept" is a conversation.

**The honesty check:** a patch with ΔE ≈ 0 is a *preference*, not a protection.
Label it as one and drop it from the ask list, or trade it away cheerfully. A
patch list padded with preferences reads as inexperienced and burns the goodwill
you need for the two asks that actually matter.

---

## Worked example

> Clause 9.2, a real shape: *"Provider shall indemnify, defend and hold harmless
> Client from any and all claims, damages, losses and expenses arising out of or
> relating to the Services."*
>
> User is the **Provider**. Contract value $48,000 over 12 months.

**Tier 1.** Severity 5 — "any and all", no cap, no negligence qualifier, and
"relating to" reaches beyond the Provider's own conduct. Likelihood 3 —
ordinary-course claims happen. Ticks: binding ✓, depended-on ✓ (interacts with
the liability cap in 11.1), trust-damaging ✓ → floor 4, already exceeded.
**Score 15 → priced.**

**Tier 2 scenarios.**

| Scenario | Description | Probability | Loss |
|---|---|---|---|
| Base | No claim. Clause never operates. | Likely (65%) | $0 |
| Stress | A third party claims the deliverable infringed; Provider funds defence. | Possible (35%) | $15k – $60k |
| Adversarial | Client is sued by its own customer over an outcome touching the Services, tenders the whole defence and settlement under "relating to". No cap applies — 11.1 is expressly carved out for indemnity. | Unlikely (12.5%) | $100k – **UNCAPPED** (modelled at $500k, the Provider's practical limit) |

`E_before = (0.35 × 15k) + (0.125 × 100k)` → `(0.35 × 60k) + (0.125 × 500k)`
= **$17.8k – $83.5k**, on a $48k contract.

That last line is the finding. The expected cost of this one clause is between
37% and 174% of everything the deal pays.

**The patch.** Three changes, in the order they matter:

1. Narrow "relating to" → "**arising out of** Provider's negligence, wilful
   misconduct, or breach of this Agreement" — restores the ordinary
   fault-based standard.
2. Delete the indemnity carve-out from the 11.1 cap, or cap indemnity at
   **2× fees paid**.
3. Add mutual indemnity for Client's own materials and instructions.

`E_after`: adversarial branch drops to Remote (2.5%) and is now capped at $96k.
= **$5.5k – $23.4k**.

**ΔE = $12.3k – $60.1k.**

**Cost-to-them:** 2. Fault-based indemnity with a cap at a multiple of fees is
the market-standard shape, not a concession. Their own outside counsel would
call the current language overreaching if asked. Change 3 is a **joint gain** —
it protects them from their own suppliers too.

→ Classified **cheap transfer**, ratio ΔE/cost ≈ 6k–30k per point.
**Ask first, ask confidently, and expect a yes.**

---

## What to write into `02_exposure/output/ledger.md`

One section per priced clause: the quoted language with its reference, the Tier
1 score with its ticks, the three scenarios as a table, `E_before`, and a
pointer to the patch. Then a summary table of all clauses with their triage
scores, so the user can see the shape of the whole document at a glance —
including how much of it is fine.
