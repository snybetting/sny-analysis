What was I trying to find out?
When i write down an EV% before placing a bet, does that actually mean anything.

What did i do?
I sorted the 1,326 bets that have EV% recorded into 5 buckets by their EV% number. I worked out what each bucket actually returned. Then for each bucket i resampled it 2,000 times to see how much that return could bounce around by luck.

What did i find?
The buckets came out in an order: lowest EV bucket returned the least, higher returned the most, no exceptions.
Each bucket is too small to trust its exact figure. The middle bucket returned 9%, but its range is -0.5% to 18.6%, so you cant say what any individual bucket truly returns.

What does this mean going forward?
I can keep using the EV% to decide which bets to take because it sorts them properly. I cant read into the specific returns per band as i need a larger sample size for that.

Results:
Aggregate: 1,326 bets. Mean claimed EV 110.65% (a 10.65% edge). Realised ROI 10.79%.

The bucket table:
EV band      n     claimed    realised    95% CI
100-105     133      3.10%      6.30%     [-11.03, 24.01]
105-110     395      7.54%      7.90%     [ -2.15, 18.31]
110-115     447     12.36%      8.97%     [ -0.96, 18.66]
115-120     161     17.08%     17.88%     [  1.06, 34.73]
120+        110     25.63%     32.30%     [  7.90, 55.22]

No prior was written before starting Q1 — unlike Q3, where I recorded my belief in advance. The method (bucketing and per-bucket bootstrapping) was new to me. Mid-analysis I predicted the buckets would come out flat, which was wrong.

Three of the five intervals contain zero, so those buckets cannot individually demonstrate a positive edge. The data-quality caveats from the Q3 findings (unrecorded pushes, correlated same-match bets) apply here too.