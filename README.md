# SNY betting results analysis

Statistical analysis of a tracked betting record - 2,600 bets on
football corners and cards, Aug 2024 to Jul 2026.

## Headline results

All-time ROI 10.35%, 95% CI [5.94, 14.78], n=2,600.

Season-on-season ROI fell 11.8 points [3.14, 20.33]. Closing line
value over the same period fell only 4.05 points [3.28, 4.82] -
so roughly a third of the decline is real edge decay and the rest
is variance. Current CLV of 8.4% against Pinnacle's close is live.

EV estimates rank correctly: realised ROI rose across all five
claimed-EV bands. Per-band intervals are 20–50 points wide, so
the ranking holds but the levels are unresolved at this sample size.

Method: bootstrap resampling, 10,000 iterations. Limitations
stated in each findings document.

## Files

- clean.py — loads the raw export, cleans it, writes clean_bets.csv
- q3.py — monthly aggregation and charts
- bootstrap.py — confidence intervals on ROI, all-time and by season
- clv.py — closing line value analysis
- pushes.py — data quality check on unrecorded pushes
- calibration.py — EV calibration and reliability plot

## Findings

- q3_findings.md — is the edge decaying, or is this variance?
- q1_findings.md — do my EV estimates mean anything?
- prior.md — beliefs recorded before each analysis

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
