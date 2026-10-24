# Decisions Log · Cleaning and Reconciliation · Brief A · Group 2

Written by: @Kshitij · Date: Oct 24, 2026

We made nine core decisions that shape the Brief A numbers; the first two define what "test volume" means.

## Reconciliation Summary

| Step | Table / Feed | Rows In | Rows Kept | Rows Rejected / Unmatched | In = Kept + Rejected? | Headline Volume (H1 2025 -> H1 2026) | Growth % | Owner |
|---|---|---|---|---|---|---|---|---|
| 0 | Raw Results Export (H1 2025 & H1 2026) | 736,127 | 736,127 | 0 | Yes | 357,769 -> 378,358 | +5.75% | Kshitij |
| 1 | Results Null Test Codes Recovery | 2,202 nulls | 2,108 recovered | 94 UNKNOWN (34 in 2025, 60 in 2026) | Yes | 357,769 -> 378,358 | +5.75% | Kshitij |
| 2 | Bookings Header Rows Removal | 557,212 | 557,197 | 15 repeated headers (7 in '25, 8 in '26) | Yes | 357,769 -> 378,358 | +5.75% | Kshitij |
| 3 | Date Format Separation (ISO vs Day-first) | 557,197 | 557,197 | 0 (recovered ~78,000 false Jul-Dec dates) | Yes | 357,769 -> 378,358 | +5.75% | Kshitij |
| 4 | Nova Jaipur & Chennai Nested Test Expansion | 26,543 bookings | 62,439 test rows | 0 | Yes | 357,769 -> 378,358 | +5.75% | Kshitij |
| 5 | City Harmonization (Bangalore -> Bengaluru) | 736,127 | 736,127 | 0 (merged spellings) | Yes | Bengaluru H1 results: 81,457 -> 88,707 | +8.90% | Kshitij |
| 6 | Nova Duplicate Rescheduled Bookings Filter | 1,500 rescheduled | Filtered from visits & booked counts | Kept in raw audit table | Yes | Lab fulfilment reconciled to 0.82-0.83 | +5.75% | Kshitij |

---

## Decisions

| # | Decision Item | Choices Considered | Chosen | Reason / Effect on Headline | Rows Affected | Reversible? | Owner |
|---|---|---|---|---|---|---|---|
| 1 | **Count basis for test volume** | Bookings table (`tests_booked`) vs. Results table (`tests_performed`) | **Results table** | The results table reflects tests actually run by the laboratory. Bookings include unfulfilled or rescheduled tests. Counting result rows gives 357,769 rows in H1 2025 and 378,358 in H1 2026 (+5.75%). | 736,127 results rows | Yes (via toggle to bookings) | Kshitij |
| 2 | **Handling package tests (PK01–PK04)** | Expand package into individual component tests vs. Count 1 result row per package | **Count 1 row per package** | No package composition master table was provided in the data pack. Package rows grew 35.18% (44,467 to 60,110), lifting package share from 12.5% to 15.9% in both channels. | 104,577 package result rows | Yes (when composition table released) | Kshitij |
| 3 | **Null test codes in results** | Drop null rows, label them `UNKNOWN`, or recover 1-to-1 from bookings table | **Recover 1-to-1 from bookings; label remaining 94 UNKNOWN** | Where exactly one null result row matched exactly one booked test on the same `booking_id`, the test code was safely imputed. Recovered 2,108 codes (1,019 in 2025, 1,089 in 2026). 94 remain UNKNOWN (34 in 2025, 60 in 2026); keeps total result volume intact. | 2,202 null test code rows | Yes | Kshitij |
| 4 | **Results with no matching booking** | Drop them, keep without city, or infer city from booking ID prefix | **Keep and assign city from prefix (e.g. `BK-AHM`, `BK-BLR`)** | They represent real clinical results (0.5% of total). Every booking ID prefix maps deterministically to one city. Channel remains unassigned (adds +0.03 pp to total growth). | 3,720 rows (1,798 in 2025, 1,922 in 2026) | Yes | Kshitij |
| 5 | **City naming inconsistency** | Keep both spellings or merge | **Merge "Bangalore" into "Bengaluru"** | Both represent the same physical market. Unmerged, Bangalore showed 0 volume in 2026 and Bengaluru showed 0 in 2025. Merged volume grew +8.90%. | 170,164 results | Yes | Kshitij |
| 6 | **Timestamp parsing strategy** | Single "mixed" parse vs. Format-aware separate parsing | **Parse ISO (+05:30) and day-first `dd/mm/yyyy` formats separately** | A naive mixed parse read `07/03/2026` as July 3rd instead of March 7th, mistakenly pushing ~78,000 bookings into July–December 2026. Separate parsing restored 100% agreement between slot month and booking ID month. | ~78,000 bookings | Yes | Kshitij |
| 7 | **Rescheduled bookings in Nova (Jaipur & Chennai)** | Count them or remove them from visit/booking counts | **Remove rescheduled duplicates from visit and booked test counts** | When a patient reschedules in Nova, a new booking ID is generated and the old one receives no results (0% fulfilment). Counting both artificially depresses the lab fulfilment rate to 0.77. Removing the 1,500 duplicates restores fulfilment across all cities to 0.82–0.83. | 1,500 booking IDs | Yes | Kshitij |
| 8 | **Results dated July or December** | Drop out-of-period rows or keep them | **Keep every row in each released H1 file** | Out-of-period result timestamps represent ~0.5% of rows (likely export boundary anomalies). Dropping or keeping them yields identical +5.75% growth. Kept for full audit reconciliation. | ~3,680 rows | Yes | Kshitij |
| 9 | **Growth tree mathematical structure** | Simple additive city/channel splits vs. Multiplicative 4-branch tree | **Multiplicative tree: Patients × Visits/Patient × Tests/Visit × Results/Test Booked** | The four branches multiply back to the total growth with exactly 0 gap: $(1 + 3.76\%) \times (1 - 0.98\%) \times (1 + 2.19\%) \times (1 + 0.72\%) = 1 + 5.75\%$. Channel contributions sum to +5.75 pp (+13.46 pp Home, -7.74 pp Clinic, +0.03 pp Unmatched). | All rows | Yes | Kshitij |

---

## Open Items

Four analytical questions remain open for Dr Menon and the commercial leadership:

1. **Package Composition Table**: Does a package count as one test or as the discrete clinical tests it bundles? Unbundling could raise true test volume growth from 5.75% to 11–13%.
2. **Plan Metric Definition**: What does the H1 2026 target (515,740) count: result rows or booked test rows? Attainment is 73.4% against results, but 89.5% against booked test rows.
3. **Root Cause of Patient Shortfall in Jaipur & Chennai**: Why were Jaipur and Chennai short of unique patients (-12.1% and -5.0%)? The data locates the gap and clears the software migration, but local commercial diagnostics are needed.
4. **Origin of 3,720 Unmatched Results**: Are these missing booking records or an off-system laboratory stream? (The first Nova bookings also appeared in March, prior to the stated April transition date).
