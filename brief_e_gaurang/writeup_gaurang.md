## 1. What was Dr Menon asking for, and what did she actually need?

Dr Menon asked whether Kalpa Health should double the budget after free home collection was associated with a reported 9% increase in bookings. However, she actually needed evidence that the campaign generated incremental bookings, attracted new patients, increased test revenue, and remained financially viable after waiver and service costs. We needed to validate the numbers before recommending whether the campaign should be scaled.

## 2. Which part was yours, and what did you produce that the group depends on?

My contribution focused on analysing booking trends, test volume, revenue, new patient registrations, and campaign-waiver usage using Python and pandas. I compared Q1 2025 with Q1 2026, calculated quarterly revenue, and measured the contribution of new patients who used the waiver. These metrics helped the group understand campaign-associated activity, although further validation and cost analysis are needed before making a final recommendation.

## 3. Which approaches did you consider, which did you choose, and why?

I considered analysing booking counts, test-level records, patient registration dates, and campaign-waiver records. I used `booking_level` for booking counts, `df` for individual test volume and revenue, `patients_df` for new registrations, and `campaign_df` for waiver usage. This approach matched each question to the appropriate dataset. I avoided treating duplicate booking IDs as rescheduling evidence because multiple tests can belong to one booking.

## 4. Which number do you trust most, its denominator, and what would make you stop trusting it?

I currently trust the calculated Q1 2026 test volume of 33,849 as a descriptive measure, provided each row in `df` represents one test. Its denominator is all test records created between 1 January and 31 March 2026. I would stop trusting it if duplicate test records, inconsistent date parsing, missing records, or different filters changed the count. I also need to reconcile the booking figures.

## 5. What broke, what did you try, and what did you change?

I encountered date-parsing issues, missing scheduled slots, and difficulty converting grouped results into DataFrames. I used explicit datetime conversion, pandas aggregation functions, and `reset_index()` where appropriate. I also discovered that booking counts and test counts showed conflicting trends. Instead of assuming the campaign caused growth, I began validating the underlying counts and separating booking-level analysis from test-level analysis.

## 6. What do you understand about a diagnostics business now that you did not before?

I now understand that bookings, tests, patients, and revenue measure different aspects of a diagnostics business. One booking can contain multiple tests, and a newly registered patient may not necessarily represent an incremental customer. Campaign-linked revenue also does not equal profit because home collection, laboratory processing, and waiver costs affect profitability. Business decisions therefore require consistent definitions and financial context, not just growth percentages.

## 7. Where did the team work well, where not, and what changes for Build 2?

Our analysis progressed by dividing the business question into measurable areas: bookings, tests, new patients, campaign usage, and revenue. However, the conflicting booking and test trends and the difference between matched and total waiver costs highlighted the need for stronger validation. For Build 2, I would agree on metric definitions first, assign clear ownership, validate joins and denominators, and review intermediate results before preparing the final recommendation.

## 8. Which Week 1 or 2 idea do you understand better after using it on this data?

I understand data aggregation and grouping much better after using pandas on this dataset. Functions such as `groupby()`, `agg()`, `nunique()`, and `reset_index()` helped me calculate quarterly bookings, test volumes, and revenue. I also learned that choosing the correct unit of analysis matters: counting rows, unique bookings, and unique patients produces different results, so the method must match the business question.

## 9. Which viva question would you least like, and your answer to it?

The question I would least like is, “Can you prove that the campaign caused the revenue increase?” My current analysis cannot prove causation. Q1 test revenue increased by 17.92%, and 46.49% of Q1 2026 test revenue was linked to campaign-waiver bookings, but these are descriptive associations. I would need a credible comparison group or another causal design, plus validated costs, to estimate incremental impact.

## 10. With two more days, what would you do first, and why?

First, I would reconcile the booking counts, investigate the reported 9% increase, and validate the campaign-waiver records against Q1 bookings. The current results show bookings falling while test volume and revenue increased, so this discrepancy must be resolved. Next, I would calculate campaign-linked revenue and waiver expenses consistently, investigate incremental contribution, and prepare a concise dashboard with definitions, assumptions, limitations, and a defensible recommendation about whether to scale the campaign.