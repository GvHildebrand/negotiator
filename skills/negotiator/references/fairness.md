# Fairness — the Concession Cost Index

> Knowing what you want is not negotiating. Knowing what it costs them is.

Every contract-review tool in existence produces a list of things that are bad
for you. That list is not a negotiating position. It is a complaint. Handed to
a counterparty it reads as greed, triggers their lawyer, and costs three weeks.

This file is what turns a findings list into a deal.

---

## 1. Price the ask from the other side

Every patch carries **ΔE** (what it saves the user, from the exposure ledger)
and **cost-to-them (1–5)** — what accepting it actually costs the counterparty.

| Cost | Meaning |
|---|---|
| 1 | Costs them nothing. Often helps them too — clarity, defined process, mutual terms. |
| 2 | Standard market shape. Their own counsel would propose it. Mild. |
| 3 | A real allocation of risk, but proportionate and defensible. |
| 4 | Meaningfully worse for them. They will want something back. |
| 5 | A major transfer. May be a dealbreaker or a signal of bad faith. |

Score cost-to-them **honestly, as their counsel would**, not as the user wishes
it were. Understating what you are asking for is how negotiations stall: you
plan for a yes, get a no, and have no give prepared.

## 2. Four classes

| Class | Shape | How to play it |
|---|---|---|
| **Joint gain** | High ΔE, cost 1. Removes ambiguity that endangers *both* parties. | Ask freely, ask first. Frame as housekeeping. These build the credit the hard asks will spend. |
| **Cheap transfer** | High ΔE, cost 2–3. Restores a market-standard allocation. | Ask early and confidently. Cite the market norm — sourced, per the factchecker. |
| **Real trade** | High ΔE, cost 4. A genuine shift of risk. | Never ask naked. Pair it with a named give from the give list, in the same sentence. |
| **Aggressive** | Cost 5, or ΔE that only exists because the counterparty behaves well. | Default: **drop it.** Keep at most one, explicitly as trade bait, and know you will lose it. |

**Preferences** — ΔE ≈ 0 — are not a class. They are noise. Cut them, or
concede them early and visibly as a gesture that costs nothing.

## 3. The ordering rule

Sort the ask list by:

```
ΔE ÷ cost-to-them
```

Highest ratio first. This single ordering does three things at once: it front-
loads what the counterparty can say yes to, it establishes the user as
reasonable before the hard ask arrives, and it means that if the negotiation
gets cut short — and it often does — the asks that landed are the ones that
mattered most per unit of friction spent.

**Cap the ask list at seven items.** More than that and the counterparty stops
reading clause by clause and starts reacting to the volume. If you have twelve
findings, the bottom five are being carried by the top seven anyway. Say what
you dropped and why, so the user can overrule you.

## 4. The give list — build it in the same pass

A matter with no give list is not ready. Before the first round, write
`03_redline/output/gives.md`: what the user is willing to concede, **priced**
with the same ledger method, in the order they should be spent.

- **Free gives** — preferences and ΔE ≈ 0 items. Spend generously and early.
  They buy real goodwill at zero cost, and the counterparty cannot tell the
  difference between a cheap concession and a gracious one.
- **Cheap gives** — small ΔE, but visibly valuable to them. This is where most
  deals are actually closed. Look hard for these: payment timing, notice
  periods, publicity rights, term length, transition assistance.
- **Real gives** — meaningful ΔE. Spend only against a Real trade ask, one for
  one, named explicitly.
- **Never** — the walk-away set. Write these down before round one, because
  the point of a walk-away is that it is decided while calm.

If you cannot find three things to give, you have not understood what the
counterparty wants. Go back and read their paper for what they were *protecting*
— the clauses they drafted most carefully tell you what they are afraid of, and
fear is the cheapest thing to reassure.

## 5. Language

The words go to a person who is deciding whether to trust the user.

- Neutral and businesslike. Never adversarial, never scolding, never clever.
- Give the **reason**, not just the edit: *"capped at 2× fees, which matches
  the liability cap in 11.1"* lands; *"unacceptable as drafted"* does not.
- Frame joint gains as mutual — because they are. "Both parties benefit from a
  defined notice period here" is true and it is disarming.
- Assume good faith in every word you write, even where the ledger's adversarial
  scenario assumed the opposite. The scenario tests the **language**; the letter
  addresses the **people**. Never let the first leak into the second.
- Never imply the counterparty drafted something in bad faith. Most one-sided
  language is a template nobody reread.

## 6. The self-check — say it out loud

Before delivering any patch list, run this and report the result to the user:

1. **Is every item class "aggressive"?** Then this is not a negotiation
   position, it is a demand. Rebuild it.
2. **Is there at least one joint gain?** If not, you have not looked for the
   shared interest. There is almost always one.
3. **Is the give list populated?** If empty, the matter is not ready.
4. **Would the user accept this list if it arrived from the other side?**
   If no — say so, in writing, to the user. This is the single most useful
   sentence in the whole deliverable, and the one no other tool will ever
   write.
5. **Does the deal still work for them?** A counterparty who signs something
   they cannot survive will not perform it. You have not won; you have bought
   a dispute with extra steps.

Point 4 is the reason this agent exists. Deliver it even when unwelcome.
