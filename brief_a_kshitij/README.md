# Build 1 · Brief A · Growth H1 2025 vs H1 2026 · Group 2

Dr Priya Menon, COO of Kalpa Health, observed that test volume grew roughly 5% in H1 2026 compared to H1 2025, but needed to know where that growth originated: whether existing patients were returning or new ones signing up, whether clinics or home collection drove the volume, and why Jaipur and Chennai missed their targets. Our analysis proves that test results grew 5.75% (378,358 rows in H1 2026 vs 357,769 in H1 2025 across six cities), driven by a 37.66% surge in home collection (+13.46 pp contribution) and a 35.18% rise in health packages (+4.40 pp contribution), masking a 12.14% drop in clinic visits (-7.74 pp) and an acute commercial patient acquisition deficit in Jaipur (-9.89%) and Chennai (+1.33%) that was not caused by their April software migration. This drives a strategic reallocation of capital toward scaling home phlebotomy fleet capacity and rebuilding regional patient acquisition networks.

## The claim

> Kalpa grew test volume by 5.75% (378,358 results across six cities in H1 2026 vs 357,769 in H1 2025), driven entirely by a 37.7% surge in home collection (+13.5 pp) and 35.2% growth in health packages (+4.4 pp), masking a 12.1% clinic volume decline (-7.7 pp) and acute patient acquisition shortfalls in Jaipur (-9.9%) and Chennai (+1.3%).

## Members and parts

| Member                 | Part of the work owned                                                                         | Notebooks                                                                           | Approach-log rows |
| ---------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------- |
| **Harshal Patil**      | Project CI/CD, Data Engineering Pipeline, DateTime Normalization & 1-to-1 Null Code Imputation | `brief_a_kshitij/notebooks/Cleanin_g_Function.ipynb`                                | Rows 1, 2, 4, 5   |
| **Kshitij Chabaria**   | Core Analytical Modeling, Growth Tree Formulation & Channel/Package Decomposition              | `brief_a_kshitij/notebooks/Cleanin_g_Function.ipynb`, `Build_Week_1_Practice.ipynb` | Rows 6, 8, 10, 12 |
| **Gaurang Khandelwal** | Regional Market Diagnostics (Jaipur & Chennai Audit), Plan Reconciliation                      | `brief_a_kshitij/notebooks/Cleanin_g_Function.ipynb`                                | Rows 3, 7, 9, 11  |

## How to run

1. Open this repository in a GitHub Codespace or local Python 3.10+ environment.
2. Open `brief_a_kshitij/notebooks/Cleanin_g_Function.ipynb` and run from a fresh kernel (**Kernel -> Restart and Run All**).
3. The headline numbers appear in Cell 51 (the Multiplicative Growth Tree) and Cell 64 (Plan vs Actual Attainment). Expected headline: **378,358 test results in H1 2026 vs 357,769 in H1 2025 (+5.75% growth)**.
4. Runtime on a fresh environment: **under 3 minutes** (~2 min 45 sec).

## Links

| What                     | Where                                                                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Video**                | [drive.google.com/drive/folders/1gcrvVFQsjLno8wPKtElHDGZDW3DNV2DK?usp=sharing](https://drive.google.com/drive/folders/1gcrvVFQsjLno8wPKtElHDGZDW3DNV2DK?usp=sharing) |
| **Slides**               | `brief_a_kshitij/slides/Build1_Slide_Template.pptx`                                                                                                                  |
| **Excel Companion**      | `slides/board_number.xlsx`                                                                                                                                           |
| **Video Transcript**     | `brief_a_kshitij/docs/video_transcript.md`                                                                                                                           |
| **Data pack provenance** | `datapack/README.md`                                                                                                                                                 |

## The logs

`brief_a_kshitij/docs/approach-log.md` · `brief_a_kshitij/docs/decisions-log.md` · `brief_a_kshitij/docs/challenges-log.md` · `brief_a_kshitij/docs/ai-log.md` · `brief_a_kshitij/docs/video_transcript.md`

## Working agreement

Nobody pushes to `main`. Every change arrives by pull request approved by a member who did not write it. Merges are merge commits so the history stays readable. Notebook outputs are cleared before commit. The build freezes the evening before presentations.
