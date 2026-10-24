# Assistant Log · Brief A · Group 2

Written by: @Kshitij · Date: Oct 24, 2026

Every use of a coding or chat assistant, one line each. Allowed uses: explaining an error you already tried to read, explaining a concept you then rewrite in your own words, checking English in the write-up without changing meaning. Not allowed: generating analysis, notebooks, cells, charts, slides, write-ups or the video script; asking what the answer or approach should be; pasting Kalpa Health data in.

| # | Date | Who | Tool | What we asked (one line) | What we did with the answer |
|---|---|---|---|---|---|
| 1 | Oct 21, 2026 | Kshitij | Claude / ChatGPT | How to write a regex mask in pandas to separate ISO 8601 strings from day-first dd/mm/yyyy strings | Used `str.match(r'^\d{2}/\d{2}/\d{4}')` to conditionally route Series parsing into separate `pd.to_datetime` branches. |
| 2 | Oct 22, 2026 | Kshitij | Claude / ChatGPT | Safest way to expand a pandas column of Python string representations of nested lists without `eval()` | Used `ast.literal_eval` wrapped in a custom explosion function to convert nested tests lists into discrete rows. |
| 3 | Oct 23, 2026 | Kshitij | Claude / ChatGPT | Mathematical condition under which multiplicative tree percentage changes reconcile with zero residual gap | Verified that $(1 + g_{\text{total}}) = \prod (1 + g_i)$ provides exact closure without requiring additive approximation residuals. |
| 4 | Oct 23, 2026 | Kshitij | Claude / ChatGPT | Meaning of `zlib.error: Error -3 while decompressing data: invalid distance too far back` when saving PPTX | Identified that saving to an open PowerPoint file with an exclusive OS write lock causes zip stream corruption; implemented in-memory `io.BytesIO` loading. |
| 5 | Oct 24, 2026 | Kshitij | Claude / ChatGPT | Grammar and conciseness check for a 50-word executive board summary sentence | Shortened phrasing from passive to active voice while strictly keeping all numbers, denominators, and dates unchanged. |
