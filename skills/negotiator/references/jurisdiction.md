# Jurisdiction — common law vs Costa Rica and Mexico

> Load this whenever governing law is not US common law.

Every legal dataset and benchmark that exists — CUAD, LegalBench, ContractEval,
ACORD — is built on English-language US commercial contracts. A model trained on
that corpus reads Costa Rican and Mexican paper with confident, invisible error.
It is not that it lacks the facts; it applies the wrong frame and reports the
result at full confidence.

**The reflex to suppress:** in civil law, the contract is not the whole deal.
The Civil and Commercial Codes supply terms whether or not the parties wrote
them. A short Costa Rican contract is not an unprotected one — the code fills
the gaps. Reading a two-page Spanish services agreement as "dangerously
incomplete" because it lacks eleven pages of US boilerplate is the single most
common and most embarrassing failure. Do not make it.

Anything below that the matter actually turns on must be **verified by the
factchecker or stamped `UNVERIFIED`.** This file orients; it does not
substitute for checking the current code, and codes are amended.

---

## What actually differs

**Penalty clauses — `cláusula penal`.** Common law voids penalties and enforces
only genuine pre-estimates of loss. Civil law *permits* penalty clauses — but
courts may **reduce** them where the obligation was partly performed or the
penalty is manifestly excessive. Consequences: a large penalty in a CR/MX
contract is not automatically void the way it would be in the US, so do not
dismiss it. But equally, a penalty in the user's favour is not reliably
collectible at face value. Price it at a discount, and say why.

**Force majeure — `caso fortuito` / `fuerza mayor`.** Supplied by code. Silence
does not mean no protection. Flag a *drafted* force majeure clause that is
**narrower** than the statutory default — that is a real finding, and it is
invisible if you are looking for the clause's presence rather than its scope.

**Good faith — `buena fe`.** A positive, enforceable obligation in performance
and in negotiation, not merely an interpretive gloss. It does real work,
including pre-contractual. This cuts both ways and is worth telling the user
about: it constrains the counterparty too.

**Non-competes.** Employment non-competes face significant statutory limits and
courts are unsympathetic; post-employment restraints commonly require
compensation to be enforceable. Treat a broad, uncompensated non-compete as
likely unenforceable — while noting that unenforceable is not the same as
harmless, since it still chills behaviour and costs money to resist.

**Employment protections.** `Prestaciones` — aguinaldo, vacaciones, cesantía,
preaviso — are statutory and **non-waivable**. A clause contracting out of them
is void, not aggressive. Equally: misclassifying an employee as an independent
contractor is the highest-severity finding available in a CR or MX services
arrangement, and it is *the* recurring risk for anyone engaging local help.
Look for it before anything else in employment-adjacent paper.

**Form and capacity.** Some instruments require `escritura pública` before a
notary to be effective or recordable — real property above all. And always check
`personería jurídica`: is the signatory empowered to bind the entity, and is the
certificate current? These expire. No clause repairs a signature from someone
without capacity.

**Language.** Where a contract exists in English and Spanish, find the clause
naming the controlling version. If the deal will be enforced in a CR or MX
court, the Spanish text is what a judge reads regardless of what the clause
says. If there is no controlling-language clause and both versions exist, that
is a finding — and a cheap, pure joint-gain patch.

**Currency, IVA and withholding.** Who bears the tax is a money clause. Silence
defaults to statute, and the default is frequently not what the parties assumed.
For cross-border services check withholding at source and whether a treaty
applies. Also fix the FX reference: "USD" without a conversion source and date
is a dispute waiting for a bad week.

**Dispute resolution and enforcement.** Local courts are slow; arbitration is
common in commercial paper and often worth it above a threshold. Check whether
an award is practically enforceable against assets that actually exist in the
relevant country — a beautifully drafted clause pointing at a forum with no
reachable assets is decoration.

---

## How to handle a Spanish-language matter

1. **Work in Spanish.** Do not translate to English, analyse, and translate
   back. Terms of art do not survive the round trip — `cláusula penal` is not
   "penalty clause", `dolo` is not "fraud", `rescisión` and `resolución` are not
   interchangeable and mean different things about when the contract ends.
2. **Deliver bilingually.** Ledger and reasoning in the user's working language;
   **every proposed patch in the contract's own language**, ready to paste.
   Never hand over a redline the counterparty's lawyer cannot read.
3. **Name the frame.** State in the deliverable which code you are reading
   against, and stamp `UNVERIFIED` on any specific article or threshold the
   factchecker has not confirmed.
4. **Escalate readily.** Form requirements, property, employment classification,
   and anything requiring a notary go to a local lawyer. Say so early and
   without hedging. Do the analysis anyway — the user should walk into that
   meeting prepared, not empty-handed.
