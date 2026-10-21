# Decisions log · cleaning and reconciliation · Brief C · Money · Group N

Every act of cleaning is a decision with a reason and an effect. Input equals clean plus rejected, every time. The headline number is recomputed after every decision so the bridge from raw to final is visible.

**Brief C question**: *Which invoices were never paid, which payments match no invoice, and how much of the gap is only timing?*

---

## Reconciliation

| Step | Table | Rows in | Rows kept | Rows rejected | In = kept + rejected? | Headline number after this step | Owner | Date |
|---|---|---|---|---|---|---|---|---|
| 0 | invoices_2026Q1 (raw) | 83630 | 83630 | 0 | Y | invoiced Q1 = raw count | | 2026-10-21 |
| 0 | invoices_2026Q2 (raw) | 83630 | 83630 | 0 | Y | invoiced Q2 = raw count | | 2026-10-21 |
| 0 | gateway Q1 (raw) | (profiled) | | | | | | 2026-10-21 |
| 0 | gateway Q2 (raw) | (profiled) | | | | | | 2026-10-21 |
| 1 | invoices (combined) | | | duplicates dropped | Y | total invoiced Rs | | |
| 2 | payments (combined, captured only) | | | failed/refunded dropped | Y | total collected Rs | | |
| 3 | LEFT JOIN invoices <- payments | | | unmatched payments isolated | Y | gap = invoiced minus collected | | |
| 4 | Timing strip (cross-quarter payments) | | | moved to timing bar | Y | hard gap Rs | | |

---

## Decisions

| # | Table | What we found | Decision | Reason | Rows affected | Effect on the headline | Reversible? | Owner |
|---|---|---|---|---|---|---|---|---|
| 1 | invoices | Amount column has thousand-separator commas e.g. "1,499.00" | Parse with thousands=',' in pd.read_csv | Prevents NaN on numeric conversion | All rows with formatted amounts | None — amounts correctly parsed | Yes | |
| 2 | payments | amount_paise column stores paise (x100 of rupees) | Divide by 100 to get rupees | Aligns units with invoice amount column for direct comparison | All payment rows | Headline amounts now comparable | Yes | |
| 3 | payments | status has values: captured, failed, refunded | Keep only captured; isolate failed/refunded in separate frame | Only captured payments represent money received | Failed rows excluded | Reduces collected-Rs figure | Yes — rejected frame retained | |
| 4 | payments | notes_invoice_ref format differs between Q1 (INV-2026-XXXXXX) and Q2 (INV2026XXXXXX) | Normalise: strip non-digits, match on numeric suffix | Allows cross-quarter join without silent mismatches | All Q2 payment rows | Increases match rate significantly | Yes — original refs preserved | |
| 5 | invoices | Checked for exact duplicate invoice_id rows | Drop exact duplicates; keep first occurrence | Same invoice billed twice inflates invoiced total | Any duplicate rows found | Decreases invoiced Rs | Yes — duplicates logged | |
| 6 | payments | Checked for duplicate payment_id rows | Drop exact duplicates; keep first occurrence | Duplicate settlement rows inflate collected total | Any duplicate rows found | Decreases collected Rs | Yes — duplicates logged | |
| 7 | payments | created_at_epoch is Unix timestamp | Convert to pd.Timestamp for period-boundary analysis | Needed to identify cross-quarter timing payments | All rows | No change to amounts; enables timing bar | Yes | |
| 8 | joined frame | Payments whose invoice date is Q2 but payment epoch falls in Q3 | Flag as timing category; separate bar in bridge | These are real revenue — timing, not leakage | Cross-quarter rows | Reduces hard-gap Rs; adds timing bar | Yes — flag column retained | |

---

## Joins

| # | Left table (rows) | Right table (rows) | Key | Type | Rows after | Keys matched more than once | Explanation of the change in count | Owner |
|---|---|---|---|---|---|---|---|---|
| 1 | invoices_all (combined Q1+Q2) | payments_captured (combined Q1+Q2) | invoice_id = normalised notes_invoice_ref | LEFT JOIN | >= invoices rows | Possible: one invoice, multiple partial payments | Extra rows = same invoice paid in split payments; aggregated before bridge | |
| 2 | invoices_all | settlements (Q1+Q2) | settlement_id | LEFT JOIN via payments | | Settlements bundle multiple payments | Used to verify fee deductions; not in headline count | |

---

## Cold runs

| Date | Who ran it | Fresh Codespace? | Runtime | Headline number | Same as last run? | If not, why |
|---|---|---|---|---|---|---|
| 2026-10-21 | (your name) | No | ~45 s | See notebook output | First run | |
