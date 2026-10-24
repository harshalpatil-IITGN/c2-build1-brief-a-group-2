# Assistant Log · Brief C · Group 2

Written by: @Harshal Patil · Date: Oct 24, 2026

Every use of a coding or chat assistant, one line each. Allowed uses: explaining an error you already tried to read, explaining a concept you then rewrite in your own words, checking English in the write-up without changing meaning. Not allowed: generating analysis, notebooks, cells, charts, slides, write-ups or the video script; asking what the answer or approach should be; pasting Kalpa Health data in.

| # | Date | Who | Tool | What we asked (one line) | What we did with the answer |
|---|---|---|---|---|---|
| 1 | Oct 21, 2026 | Harshal | Claude / ChatGPT | How to properly parse currency string columns formatted with commas in `pd.read_csv` without converting to NaN | Added `thousands=','` argument to `pd.read_csv`, ensuring numeric float conversion on initial load. |
| 2 | Oct 21, 2026 | Harshal | Claude / ChatGPT | Why a `LEFT JOIN` produces more rows than the left DataFrame and how to detect duplicate keys | Used `.duplicated(subset=['invoice_id'])` to identify retry attempts on single invoices, then pre-aggregated payments by invoice ref before joining. |
| 3 | Oct 21, 2026 | Harshal | Claude / ChatGPT | Syntax for converting Unix millisecond timestamp columns to pandas datetime with timezone awareness | Applied `pd.to_datetime(df['created_at_epoch'], unit='s', utc=True)` to enable cross-quarter timing analysis. |
| 4 | Oct 22, 2026 | Harshal | Claude / ChatGPT | How to construct a financial waterfall bridge chart using matplotlib bar containers with intermediate cumulative bottoms | Wrote custom matplotlib bar script calculating bottom offsets: `bottom[i] = cumulative[i-1]` for positive and negative deltas. |
| 5 | Oct 24, 2026 | Harshal | Claude / ChatGPT | Syntax for applying border styles and number formats across openpyxl worksheet column ranges | Used `openpyxl.styles.Border` and `Side(style='thin')` in a loop across active worksheet cells in `create_board_number_excel.py`. |
