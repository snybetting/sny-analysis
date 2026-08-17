Question:
Is my edge decaying, or is this variance? Decided on feel and rough analysis until now.

On 7 August 2026, written before i ran the math, i predicted my edge was roughly 8% and pretty much stable.

Method: 
Bootstrap resampling, 10,000 iterations on 2,600 tracked bets from August 2024 to July 2026. I paired a difference test between seasons. I also calculated the CLV against Pinnacle closing lines on the 1,364-bet covered subset. 

Results: 
All-time: 10.35% ROI, 95% CI [5.94, 14.78], n=2,600
24/25: 17.63%, 95% CI [11.52, 23.78], n=1,191
25/26: 5.86%, 95% CI [-0.25, 11.92], n=1,409
Difference: 11.82 points, 95% CI [3.14, 20.33] — excludes zero

CLV (n=1,326, multiples excluded): 24/25 12.45%, 25/26 8.40%
Difference: 4.05 points, 95% CI [3.28, 4.82] — excludes zero

Why CLV:
CLV is more important than ROI because ROI depends on whether the bets won or not. CLV is settled the moment the market closes - you either beat the closing price or you didn't, regardless of the outcome. It measures your edge directly rather than your edge + luck. The CLV difference interval was [3.28, 4.82] - 1.5 points wide - while the ROI difference was [3.14, 20.33] at 17 points wide. Same underlying question, ten times the precision. Past ROI tells you what happened, beating the closing line tells you you've found something the sharpest market hadn't priced in yet.

Decomposition:
ROI fell 11.8 points and CLV fell 4.05. Roughly a third real deterioration, two thirds variance. My original "end of S-curve" position and my August 14 "it's all variance" position were wrong. 

Conclusion:
The career edge is established and excludes zero; the decline is real but a third the size the returns implied; 8.4% against the sharpest close in the market is material.

What changes?
My 7 August stop condition was 50 bets a month. This proved that rule doesn't survive a pre-season (June/July), and it needs restating as a rolling average.
I didn't have any CLV tracking before this, i now know it's a far tighter measure than ROI - the interval was a tenth the width. Tracking it prospectively from September is a change, and it's the most useful thing this analysis has produced. 

Limitations:
~40% of bets were on whole lines where pushes are possible but were not recorded in the source data. The non-pushable subset (n=1,559) returns 12.66% [6.85, 18.50], overlapping the full-sample interval, so the effect does not appear material at this sample size.
81 of the 2,600 rows are doubles, trebles and accas. They're included in all figures above. They stake £36.95 and return −£0.58 (−1.57% ROI); excluding them lifts all-time ROI from 10.35% to 10.50%. Kept in for Q3 because it's real money staked. They would need excluding from any calibration or CLV work, since a multiple's combined price doesn't correspond to a single event.
The bootstrap resamples individual bets, which assumes independence. Mine aren't independent — I regularly take two or three lines on the same match and they resolve together. The record therefore contains less independent information than 2,600 separate bets would, and the true confidence intervals are wider than those reported. Not corrected; noted.
CLV coverage was 63% of bets in 24/25 and 44% in 25/26. To check the covered subset was representative, I compared its ROI against the full seasons: 15.13% vs 17.63% and 5.57% vs 5.86%. Close enough that the subset doesn't appear biased.