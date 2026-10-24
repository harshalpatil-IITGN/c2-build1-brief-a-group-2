# Video Presentation Transcript · Brief A (Growth H1 2025 vs H1 2026) · Group 2

**Format**: Three-member Group Video Presentation  
**Total Target Length**: 20 to 30 minutes (7 to 9 minutes per member)  
**Notebook Referenced**: `brief_a_kshitij/notebooks/Cleanin_g_Function.ipynb`  
**Handbook Standard**: Formatted strictly to Build 1 Project Handbook specifications (Page 24/30).

---

## Recording Guidelines for the Team

> [!IMPORTANT]
> **Strict Handbook Rules**:
> 1. **Screen and Face**: Name and part owned displayed on the first frame. One take per member section.
> 2. **Pacing**: Say all numbers slowly, with their denominators, so a viewer or panelist can pause and verify.
> 3. **Cell Execution**: Do not scroll code or explain syntax. Switch to the notebook, run the cell that produces the number, state the finding, and move on.
> 4. **No Overlap**: Never recap the brief history, never read slides aloud, and never repeat what a teammate covered.

---

## Member 1: Kshitij Chabaria (0:00 – 8:00)

**Role**: Lead Analyst · Core Analytical Modeling, Growth Tree & Channel Decomposition  
**Part Owned**: The Multiplicative Growth Tree, Channel Shift & Package Surge  
**Primary Notebook**: `brief_a_kshitij/notebooks/Cleanin_g_Function.ipynb` (Cells 51, 56)

---

### Frame 1: Title & Role [0:00 – 0:30]
*[Screen showing speaker camera feed alongside Slide 3 (`slide3_growth_tree.png`) with title: "Kshitij Chabaria · Core Analytical Modeling & Growth Tree Decomposition"]*

> "Hello, my name is Kshitij Chabaria, and I am the lead analyst on Brief A for Group 2. My responsibility was formulating the growth model, constructing the multiplicative growth tree, and decomposing the volume expansion across channels and product packages."

---

### 1. The Question in My Words & Prior Prediction [0:30 – 2:00]
> "In my own words, Dr Menon observed that Kalpa Health grew test volume by roughly five percent in the first half of 2026. But a top-line five percent is dangerous without knowing the mechanism: did we attract new patients, or did existing patients return more frequently? Did our clinic network drive the expansion, or was it home collection? And why were Jaipur and Chennai missing their targets?
> 
> Before opening the dataset, my initial hypothesis was that growth was driven by existing patients returning to our physical clinic network following post-pandemic normalization, and that clinics would account for more than eighty percent of total test volume. 
> 
> The data proved that guess completely wrong: clinic volume did not grow at all—it suffered a severe contraction of **-12.14%**, while home collection surged by **+37.66%**, entirely carrying the company's growth."

---

### 2. One Decision, The Alternative Rejected & Reason (Point at Log Row) [2:00 – 3:45]
*[Screen switches to `brief_a_kshitij/docs/decisions-log.md` showing Row 9 and `Cleanin_g_Function.ipynb` Cell 51]*

> "The core decision I own is documented in **Decisions Log Row 9** and **Approach Log Row 8**: structuring our analysis around a **Multiplicative Four-Branch Growth Tree**:
> $$\text{Results} = \text{Unique Patients} \times \frac{\text{Visits}}{\text{Patient}} \times \frac{\text{Tests Booked}}{\text{Visit}} \times \frac{\text{Results}}{\text{Test Booked}}$$
> 
> *[Executes Cell 51 in `Cleanin_g_Function.ipynb`]*
> 
> The alternative I considered and rejected was a simple additive rate-and-volume mix or independent city-level volume aggregations. 
> 
> The reason I rejected additive splits is that they cannot separate commercial patient demand from operational laboratory fulfilment. In our multiplicative tree, the product of the four branches multiplies back to the actual total growth with an exact mathematical gap of zero:
> - Unique Patients: grew **+3.76%** (from 204,444 to 212,126 unique patient IDs).
> - Visits per Patient: contracted slightly by **-0.98%** (from 1.488 to 1.474 visits).
> - Tests Booked per Visit: expanded by **+2.19%** (from 1.411 to 1.442 tests).
> - Results per Test Booked: remained stable, up **+0.72%** (from 0.832 to 0.838).
> 
> $(1 + 0.0376) \times (1 - 0.0098) \times (1 + 0.0219) \times (1 + 0.0072) = 1 + 0.0575$, or exactly **+5.75%**."

---

### 3. One Number I Trust, Its Denominator & What Would Break It [3:45 – 5:30]
*[Screen displays Cell 51 output table and Slide 5 Panel A]*

> "The number I trust most in this entire study is **+37.66% Home Collection Results Growth**, which contributed **+13.46 percentage points** to our total top-line growth.
> 
> Its denominator is **110,929 test results** attributed to home collection visits in H1 2025, compared against **152,709 test results** in H1 2026 across all six cities. 
> 
> What would make me stop trusting this number: if phlebotomists who performed home blood draws were logging visits under clinic walk-in codes in the legacy system, or conversely, if the 3,720 orphan results with no matching booking ID turned out to belong entirely to physical clinics rather than being split proportionately."

---

### 4. One Thing That Broke (Point at Challenges Entry) [5:30 – 7:00]
*[Screen switches to `brief_a_kshitij/docs/challenges-log.md` showing Row 9 and Cell 56 in `Cleanin_g_Function.ipynb`]*

> "The issue that broke our initial volume estimation is recorded in **Challenges Log Row 9**: **Package tests masking clinical laboratory test volume**.
> 
> *[Executes Cell 56 in `Cleanin_g_Function.ipynb`]*
> 
> In our results tables, package tests with codes `PK01` through `PK04` grew by **+35.18%**, jumping from **44,467** rows to **60,110** rows, lifting package share from **12.43%** to **15.89%** of all results. Meanwhile, routine non-package tests grew by just **+1.58%**.
> 
> However, each package appears as exactly one row in the results table. If each package bundles four to six individual clinical tests, counting raw result rows substantially understates true laboratory workload. 
> 
> Because Kalpa provided no official package composition dictionary in the data pack, we avoided making speculative assumptions. We preserved the auditable row count at +5.75% and formally documented that true clinical test volume grew between **11% and 13%**."

---

### 5. What I Would Do with Two More Days [7:00 – 8:00]
> "If I had two more days on this project, I would obtain the official clinical package composition table from the laboratory director. I would unbundle the 60,110 package rows into discrete analyte tests, re-running our growth tree at the clinical test level to evaluate instrument throughput and reagent supply chain constraints across each city's central lab."

---

## Member 2: Harshal Patil (8:00 – 16:00)

**Role**: Pipeline Engineer · Data Ingestion, Timestamp Harmonization & Null Imputation  
**Part Owned**: Data Engineering Pipeline, DateTime Normalization & 1-to-1 Null Code Imputation  
**Primary Notebook**: `brief_a_kshitij/notebooks/Cleanin_g_Function.ipynb` (Cells 18, 19, 43, 49)

---

### Frame 1: Title & Role [8:00 – 8:30]
*[Screen showing speaker camera feed alongside slide displaying: "Harshal Patil · Data Pipeline Engineering, Ingestion & Null Recovery"]*

> "Hello, I am Harshal Patil. My responsibility on Brief A was building the data ingestion, validation, and harmonization pipeline that ingested over 1.3 million records across our bookings and results tables to ensure every downstream calculation sat on verified data."

---

### 1. The Question in My Words & Prior Prediction [8:30 – 10:00]
> "In my words, Dr Menon needed to know whether the five percent growth figure was a genuine operational reality or an artifact of system noise, duplicate entries, and corrupted feeds across disparate software systems.
> 
> Before opening the raw data, my prediction was that data ingestion would be straightforward with standard pandas parsers, and that missing values would be under one percent and easily handled by dropping null rows.
> 
> That prediction was completely invalidated within our first hour: dropping nulls would have discarded over 2,200 real clinical tests, and naive date parsing corrupted tens of thousands of records across quarters."

---

### 2. One Decision, The Alternative Rejected & Reason (Point at Log Row) [10:00 – 11:45]
*[Screen switches to `brief_a_kshitij/docs/decisions-log.md` showing Row 3 and `Cleanin_g_Function.ipynb` Cell 18]*

> "The primary cleaning decision I own is documented in **Decisions Log Row 3** and **Approach Log Row 2**: **Deterministic 1-to-1 Null Test Code Recovery**.
> 
> *[Executes Cell 18 and Cell 19 in `Cleanin_g_Function.ipynb`]*
> 
> In the raw results feeds, 2,202 rows arrived with null test codes (1,053 in 2025 and 1,149 in 2026).
> 
> The alternatives I considered and rejected were:
> 1. Dropping the rows: rejected because dropping would erase verified laboratory tests actually conducted on patients.
> 2. Imputing the most common test code (modal imputation): rejected because guessing clinical test codes corrupts medical diagnostic integrity.
> 
> Instead, I implemented a strict 1-to-1 matching algorithm in `recover_missing_test_codes()`. We joined results back to bookings on `booking_id`. Where an invoice had exactly one null result row and exactly one unmatched booked test, we recovered the code. This recovered **2,108 test codes** (1,019 in 2025 and 1,089 in 2026). Exactly 94 unresolvable cases were labelled `UNKNOWN` to keep total volume balanced."

---

### 3. One Number I Trust, Its Denominator & What Would Break It [11:45 – 13:30]
*[Screen displays Cell 4 output showing shape and total row count]*

> "The number I trust most is the total audited H1 2026 result volume of **378,358 test results**, representing an increase of **20,589 results** (+5.75%) over the H1 2025 baseline of **357,769 results**.
> 
> Its denominator is the complete, deduplicated set of all verified laboratory result rows generated between 1 January 2026 and 30 June 2026 across all six operating cities.
> 
> What would break it: approximately 0.5% of result rows carry timestamps in July or December due to laboratory batch export cutoffs. If laboratory operations proved that these rows were duplicate QC calibration runs rather than billed patient samples, the headline count would adjust, although our sensitivity analysis confirms net growth remains stable at +5.75%."

---

### 4. One Thing That Broke (Point at Challenges Entry) [13:30 – 15:00]
*[Screen switches to `brief_a_kshitij/docs/challenges-log.md` showing Row 4 and `Cleanin_g_Function.ipynb` Cell 43]*

> "The most dangerous issue that broke during pipeline construction is documented in **Challenges Log Row 4**: **Mixed timestamp formats leaking across quarter boundaries**.
> 
> *[Executes Cell 43 in `Cleanin_g_Function.ipynb`]*
> 
> When we first executed `pd.to_datetime()`, the bookings tables showed booking dates stretching all the way into December 2026! Over **78,000 bookings** appeared to sit in the second half of the year.
> 
> The failure occurred because the export contained two conflicting formats: ISO 8601 strings with a `+05:30` timezone offset, and day-first `dd/mm/yyyy HH:MM` strings. The default parser read `07/03/2026` as July 3rd instead of March 7th.
> 
> I wrote the `parse_ts()` function in Cell 43, applying regex guards to separate day-first patterns from ISO strings. When validated against booking ID timestamp prefixes, our date reconciliation achieved **100% agreement**, restoring all 78,000 records to their true H1 months."

---

### 5. What I Would Do with Two More Days [15:00 – 16:00]
> "With two more days, I would package our ingestion functions into a strict Pydantic-based validation library (`src/kalpa/loaders.py`). I would enforce runtime schema checks on column types, regex ID patterns, and timestamp formats so that format inconsistencies are blocked and logged before entering the analytical pipeline."

---

## Member 3: Gaurang Khandelwal (16:00 – 24:00)

**Role**: Market Diagnostics & Strategy · Regional Analysis, Software Audit & Plan Reconciliation  
**Part Owned**: Regional Market Diagnostics (Jaipur/Chennai Audit), Nova Rescheduled Filter & Plan Reconciliation  
**Primary Notebook**: `brief_a_kshitij/notebooks/Cleanin_g_Function.ipynb` (Cells 27, 57, 64)

---

### Frame 1: Title & Role [16:00 – 16:30]
*[Screen showing speaker camera feed alongside slide displaying: "Gaurang Khandelwal · Regional Market Diagnostics, Software Audit & Strategic Recommendations"]*

> "Hello, my name is Gaurang Khandelwal. My focus on Brief A was conducting the regional forensic audit of Jaipur and Chennai, evaluating the impact of the Nova software migration, reconciling actuals against plan, and defining Dr Menon’s strategic action plan."

---

### 1. The Question in My Words & Prior Prediction [16:30 – 18:00]
> "In my words, Dr Menon specifically asked why Jaipur and Chennai missed their targets so severely, and leadership’s prevailing suspicion was that the newly implemented Nova booking software was failing and losing records.
> 
> Before opening the data, my prediction was that technical integration glitches during the software cutover were indeed the root cause of the shortfall, and that once we corrected for dropped booking IDs, Jaipur’s growth rate would align with the other cities.
> 
> That prediction was completely disproved by our audit: the software functioned properly, and the shortfall was an authentic collapse in patient acquisition."

---

### 2. One Decision, The Alternative Rejected & Reason (Point at Log Row) [18:00 – 19:45]
*[Screen switches to `brief_a_kshitij/docs/decisions-log.md` showing Row 7 and `Cleanin_g_Function.ipynb` Cell 57]*

> "The critical analytical decision I own is documented in **Decisions Log Row 7** and **Approach Log Row 7**: **Filtering out 1,500 rescheduled duplicate bookings in the Nova booking system**.
> 
> *[Executes Cell 57 in `Cleanin_g_Function.ipynb`]*
> 
> In Jaipur and Chennai, the apparent ratio of results per test booked dropped to **0.77**, compared to **0.83** in other cities, which looked like proof that the new software was losing lab results.
> 
> The alternative considered was treating these bookings as unfulfilled tests or lab failures.
> 
> By auditing `status_at_export`, I discovered that when a patient reschedules in Nova, the system creates a brand-new booking ID while retaining the original ID marked as `rescheduled`. The original ID never receives lab results (0% fulfilment).
> 
> Filtering out these **1,500 duplicate rescheduled records** eliminated the artificial denominator inflation. Immediately, laboratory fulfilment in Jaipur and Chennai rose to **0.825 and 0.833**, perfectly matching Ahmedabad and Bengaluru. This proved the laboratory was fulfilling every real sample received."

---

### 3. One Number I Trust, Its Denominator & What Would Break It [19:45 – 21:30]
*[Screen displays Cell 64 output showing the plan comparison table]*

> "The number I trust most is **73.0% Overall Plan Attainment on Results** (376,443 actual results against the 515,740 plan target), with **Jaipur achieving only 63.6%** and **Chennai achieving only 70.4%**.
> 
> Its denominator is the **515,740 test target** established in `plan_2026_H1.csv` across our six cities.
> 
> *[Executes Cell 64 in `Cleanin_g_Function.ipynb`]*
> 
> What would break it: Cell 64 reveals a profound budgeting discovery. When we evaluate actual performance against *booked test rows* (458,109 booked tests), attainment jumps to **88.8%**! 
> 
> In fact, the plan was constructed by applying an exact **+18.0% YoY growth factor to H1 2025 booked rows** in every city. If corporate finance intended the plan to measure booked demand rather than lab results, then attainment was 88.8%, not 73.0%."

---

### 4. One Thing That Broke (Point at Challenges Entry) [21:30 – 23:00]
*[Screen switches to `brief_a_kshitij/docs/challenges-log.md` showing Row 1 and `Cleanin_g_Function.ipynb` Cell 27]*

> "The technical challenge that broke our initial schema ingestion is documented in **Challenges Log Row 1**: **Nova nested JSON structures in Jaipur and Chennai**.
> 
> In April 2026, 26,543 booking rows arrived with `test_code` as null because booked tests were stored as a nested JSON list `[{'code': '...', 'price': ...}]`, while patient identifiers were embedded inside a nested dictionary.
> 
> *[Executes Cell 27 in `Cleanin_g_Function.ipynb`]*
> 
> Reading these tables naively left 154 null result codes unrecoverable. 
> 
> I wrote the unnesting logic in Cell 27 to explode the nested tests list into discrete rows and extract `patient_id`. This expanded the data into **62,439 clean test rows** and brought unresolvable null test codes down from 154 to just 8.
> 
> Furthermore, we proved software was not the cause of Jaipur’s **-9.89%** drop through four checks:
> 1. The deficit existed in **January 2026** (-0.2% vs +9.5% other cities), three months before Nova launched.
> 2. Returning patient retention was higher in Jaipur (**37.4%**) and Chennai (**35.8%**) than elsewhere (~30%).
> 3. Patient ID syntax was identical.
> 4. Lab fulfilment was rock-solid at **83%**."

---

### 5. What I Would Do with Two More Days [23:00 – 24:00]
> "With two more days, I would travel to Jaipur and Chennai to audit local clinic partner referral networks and corporate tie-ups. Because existing patients are returning at healthy rates (over 35%), the problem is entirely top-of-funnel customer acquisition. I would interview clinic managers to determine why new patient signups dropped by **12.1%** in Jaipur and **5.0%** in Chennai, designing localized digital acquisition campaigns for Monday morning."

---

## Part 4: Group Conclusion & Transition to Viva [24:00 – 24:30]

*[Screen switches back to full-team camera view with Slide 8 displaying repository links]*

### Speaker 1: Harshal Patil
> "To conclude: Kalpa grew **5.75%** in H1 2026, propelled entirely by a **+37.7%** surge in home collection and **+35.2%** package adoption, masking clinic volume declines of **-12.1%** and patient acquisition shortfalls in Jaipur and Chennai.
> 
> All notebooks, cleaning scripts, logs, and artifacts are frozen and open in our repository. We thank you and are ready for the panel's viva questions."

---

## Technical Summary Matrix for Panel Review

| Metric / Dimension | H1 2025 Baseline | H1 2026 Actual | YoY Growth | Growth Contribution | Log Reference |
|---|---|---|---|---|---|
| **Total Test Results** | 357,769 | 378,358 | **+5.75%** | +5.75 pp | Decisions Log Row 1 |
| **Unique Patients** | 204,444 | 212,126 | **+3.76%** | Tree Branch 1 | Approach Log Row 8 |
| **Visits per Patient** | 1.4883 | 1.4737 | **-0.98%** | Tree Branch 2 | Approach Log Row 8 |
| **Tests per Visit** | 1.4111 | 1.4420 | **+2.19%** | Tree Branch 3 | Approach Log Row 8 |
| **Results per Booked Test** | 0.8322 | 0.8382 | **+0.72%** | Tree Branch 4 | Approach Log Row 8 |
| **Home Collection Results** | 110,929 | 152,709 | **+37.66%** | **+13.46 pp** | Decisions Log Row 9 |
| **Clinic Results** | 245,042 | 223,727 | **-12.14%** | **-7.74 pp** | Decisions Log Row 9 |
| **Package Tests (PK01–04)** | 44,467 | 60,110 | **+35.18%** | **+4.40 pp** | Decisions Log Row 2 |
| **Jaipur Total Results** | 36,950 | 33,297 | **-9.89%** | Plan Attain: 63.6% | Challenges Log Row 8 |
| **Chennai Total Results** | 65,243 | 66,108 | **+1.33%** | Plan Attain: 70.4% | Challenges Log Row 8 |
