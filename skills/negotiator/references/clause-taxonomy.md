# Clause taxonomy — what to look for

Grounded in **CUAD** (Contract Understanding Atticus Dataset, 510 commercial
contracts, 13k expert labels, 41 categories — Hendrycks et al., NeurIPS 2021,
<https://github.com/The-Atticus-Project/cuad>), reorganised by *what actually
costs money* rather than alphabetically, and extended for civil-law instruments
CUAD does not cover.

CUAD is a US commercial corpus. It is excellent for what it contains and blind
to everything else. Section 4 exists because of that blindness.

---

## 1. The money clauses — always price these

These carry the exposure. If you price nothing else, price these.

| Category | The failure mode |
|---|---|
| **Uncapped Liability** | The single highest-value finding available. Never blur into a number — write `UNCAPPED`. |
| **Cap On Liability** | Check the *carve-outs*. A 12-month cap with indemnity, IP, and confidentiality carved out is not a cap. |
| Indemnification | "Any and all" + "relating to" + no fault standard = the worked example in the ledger. |
| **Liquidated Damages** | In civil law jurisdictions see §4 — this is a different animal there. |
| Minimum Commitment | Take-or-pay. Model against realistic volume, not hoped-for volume. |
| Revenue/Profit Sharing | Check the *definition* of the base. Gross vs net is the whole clause. |
| Price Restrictions / MFN | Most Favored Nation binds your future pricing to your worst past deal. |
| Insurance | Required limits the user may not carry. Cheap to miss, expensive to breach. |

## 2. The trap clauses — cheap to fix now, brutal later

Low salience on a first read, high severity when they operate.

- **Auto-renewal + Notice Period To Terminate Renewal** — the classic. A 90-day
  notice window on a 12-month auto-renew means eight months of the year the user
  cannot exit. Always cross-check renewal term against notice period.
- **Termination For Convenience** — check whether it is *mutual*. One-sided
  convenience termination against a provider is a revenue clause, not an admin one.
- **Anti-Assignment / Change of Control** — can block the user's own sale or
  restructure. Existential for anyone who might ever exit.
- **Non-Compete / Exclusivity / No-Solicit** — scope, duration, geography.
  Frequently unenforceable and still chilling; see §4 for jurisdiction.
- **Audit Rights** — check notice, frequency, scope, and who pays.
- **Post-Termination Services** — unpaid transition obligations that outlive revenue.
- **Irrevocable Or Perpetual License** — perpetuity is forever, including after the relationship ends badly.
- **Covenant Not To Sue / Third Party Beneficiary** — quiet waivers of remedy.

## 3. The structural clauses — read them, rarely fight them

Governing Law, Agreement/Effective/Expiration Date, Parties, Document Name,
Renewal Term, ROFR/ROFO/ROFN, IP Ownership Assignment, Joint IP Ownership,
License Grant and its variants (Non-Transferable, Affiliate Licensor/Licensee,
Unlimited), Source Code Escrow, Warranty Duration, Non-Disparagement,
Competitive Restriction Exception, Volume Restriction.

Read all of them. Flag only where they interact badly with §1 or §2 — for
example IP assignment reaching the user's pre-existing tooling, or governing law
in a forum where enforcement is impractical for a deal this size.

**The interaction check matters more than any single clause.** The most common
serious finding is not one bad clause; it is a reasonable cap in 11.1 quietly
disabled by a carve-out in 9.2. Always read the cap and the indemnity together,
the renewal and the notice period together, and the IP grant against the
confidentiality survival period.

## 4. Civil-law additions — CUAD does not have these

**Load `jurisdiction.md` whenever governing law is not US common law.**
For Costa Rican and Mexican paper, additionally check:

- **Cláusula penal** — the civil-law penalty clause. Not the same as liquidated
  damages, and judicially reducible. See `jurisdiction.md`.
- **Caso fortuito / fuerza mayor** — force majeure is partly supplied by code,
  so a silent contract is not an unprotected one.
- **Personería jurídica** — is the signatory actually empowered to bind the
  entity? Verify against the *personería* certificate, and check its date;
  they expire. A contract signed by someone without capacity is a problem no
  clause fixes.
- **Form requirements** — some instruments require *escritura pública* before a
  notary to be effective or recordable. Private signature is not always enough.
- **Jornada / prestaciones laborales** — employment protections are statutory
  and non-waivable. A clause contracting out of them is void, not aggressive.
- **IVA and withholding** — who bears the tax is a money clause. Silence
  defaults to statute, and the default is often not what the parties assumed.

## 5. By instrument — the first-pass checklist

- **NDA** — definition of Confidential Information (is it bounded?), term of
  obligation vs term of agreement, residuals clause, return/destruction,
  carve-outs, whether it is *mutual*, injunctive relief.
- **MSA / SSA** — cap and its carve-outs, indemnity, IP in deliverables vs
  background IP, acceptance criteria, payment terms and late interest,
  termination and its notice, post-termination transition.
- **Supplier / purchase order** — Incoterms, title and risk transfer, inspection
  and rejection window, warranty duration, remedy for defect, HS classification
  and duties, currency and FX risk.
- **Lease** — escalation formula, restoration obligation at exit, assignment and
  subletting, quiet enjoyment, who insures what, deposit return mechanics.
- **Employment / contractor** — classification risk first, then IP assignment,
  non-compete enforceability, termination and statutory severance.
- **LOI / term sheet** — **which parts are binding.** Exclusivity, confidentiality
  and expenses usually are; everything else usually is not. Get this wrong and
  a "non-binding" document is a contract.

## 6. Missing provisions

Absence is a finding. Run the instrument checklist above and report what is
*not* there — a missing liability cap is worse than a bad one, and it will not
appear in any clause-by-clause scan because there is no clause to scan.
