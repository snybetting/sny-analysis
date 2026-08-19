Question: does beating the closing line actually translate into profit in my record?

Method: I split 1,326 bets with a closing line at the median CLV, then compared realised ROI either side. I bootstrapped the difference and ran 10,000 iterations.

Results: low half resulted in a mean CLV of 5.45%, ROI 5.43%, n=665. The higher half resulted in a mean CLV of 15.89%, ROI 16.27%, n=661. The difference = 10.81 points, 95% CI [-0.92, 22.55]. Average odds 1.98 and 2.09, so the price isn't driving it.

Conclusion: the point estimates line up almost identically, the realised ROI tracks the mean CLV to within a fraction of a point in both halves. But the difference test doesn't clear zero, so this is consistent with CLV predicting profit rather than proof of it. The power analysis explains why: 663 bets per side can't resolve a 10-point ROI gap.

Five-bucket version (265 bets each): ROI by CLV band came out 5.31%, 11.58%, -0.72%, 14.41%, 23.61%. Directionally right at the extremes but the middle bucket breaks the pattern — a good example of what 265-bet subsets can and can't show.

Caveat: CLV and profit are both derived from the odds I took, so this isn't a fully independent test. Bets where I got a good price relative to the close tend to be bets where I got a good price.