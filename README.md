# SNY betting results analysis

Statistical analysis of a tracked betting record - 2,600 bets on
football corners and cards, Aug 2024 to Jul 2026.

## Headline results

2,600 bets, 3,008.88 units staked, 311.36 units profit. ROI 10.35%, 95% CI [5.94, 14.78].

Season-on-season ROI fell 11.8 points [3.14, 20.33]. Closing line
value over the same period fell only 4.05 points [3.28, 4.82] -
so roughly a third of the decline is real edge decay and the rest
is variance. Current CLV of 8.4% against Pinnacle's close is live.

EV estimates rank correctly: realised ROI rose across all five
claimed-EV bands. Per-band intervals are 20-50 points wide, so
the ranking holds but the levels are unresolved at this sample size.

Corners and cards decayed by similar amounts in CLV terms, despite
very different ROI outcomes.

Monte Carlo power analysis shows ROI cannot be measured precisely
enough to manage on: at 2,600 bets a true 10% edge lands anywhere
in [5.0, 15.4], and even 50,000 bets leaves a 2.3-point band.

Bets in the top half by CLV returned 16.27% against 5.43% for the
bottom half, with realised ROI tracking mean CLV closely in both.
The difference does not clear zero at 95% confidence - consistent
with CLV predicting profit, not proof of it.

Method: bootstrap resampling and Monte Carlo simulation, 2,000 to
10,000 iterations. Limitations stated in each findings document.

## Files
- clean.py - loads the raw export, cleans it, writes clean_bets.csv
- q3.py - monthly aggregation and charts
- bootstrap.py - confidence intervals on ROI, all-time and by season
- clv.py - closing line value analysis
- pushes.py - data quality check on unrecorded pushes
- calibration.py - EV calibration and reliability plot
- drawdown.py - equity curve and drawdown analysis
- markets.py - corners vs cards split
- power.py - Monte Carlo power analysis: how precisely can ROI be measured?
- clv_calibration.py - does CLV predict profit?

## Findings
- q3_findings.md - is the edge decaying, or is this variance?
- q1_findings.md - do my EV estimates mean anything?
- drawdown_findings.md - how deep and how long are the bad runs?
- markets_findings.md - does the edge differ between corners and cards?
- power_findings.md - how many bets before ROI means anything?
- clv_calibration_findings.md - does beating the close translate into profit?
- prior.md - beliefs recorded before each analysis

## Tooling

I could not have done this without Claude LLM. The method - bootstrap
resampling, the paired difference test, CLV as a lower-variance
measure than ROI - was not something I knew existed. Claude
explained each step and I typed the code myself rather than
generating it, but I would not have got here alone.

What is mine: the questions, the domain judgements about the
betting markets, the priors written before each analysis, and the
interpretation. Where my predictions were wrong - I expected the
season decline to be variance, and the EV bands to come out flat -
the results are reported as they came out.

This is a first attempt. I am learning the statistics as I go.
