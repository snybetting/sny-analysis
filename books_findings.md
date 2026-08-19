Question: does my edge differ between Bet365 and Flutter?

Method: I grouped Paddy Power, Sky Bet, Flutter and Betfair as one 'Flutter' entity. I dropped William Hill, Unibet and SpreadEx - just 8 bets total between them. I then compared CLV on bets with a closing line, and ROI and volume on the full sample.

Results: 

CLV (bets with a closing line):
book      season    CLV      ROI      odds     n
Bet365    24/25    12.31%   12.29%    1.96    671
Bet365    25/26     7.38%    3.52%    1.95    386
Flutter   24/25    14.00%   41.77%    2.20     58
Flutter   25/26    10.34%   13.27%    2.40    203

Full sample (all bets):
book      season    ROI      odds     n
Bet365    24/25    13.85%    2.35    1048
Bet365    25/26     6.56%    1.99     744
Flutter   24/25    50.17%    4.08     116
Flutter   25/26     5.17%    3.08     598

Conclusion: Three things:

- CLV is near-identical between books all-time (10.51% vs 11.16%), so neither is a materially better source of value.
- Both books' CLV fell by a similar amount season on season - Bet365 12.31 → 7.38, Flutter 14.00 → 10.34. The decline isn't specific to one account.
- But volume shifted hard: Bet365 1,048 → 744 bets, Flutter 116 → 598. And Flutter's average odds are much longer (3.08 vs 1.99 in 25/26), so the betting mix moved toward higher-variance bets. That's part of why 25/26 returns looked worse than the CLV decline alone would explain.

Caveats: CLV figures cover only 57% of Bet365 bets and 35% of Flutter's, and I haven't checked whether those bets are typical of the rest. Flutter's 24/25 cell is 58 bets on CLV and 116 on the full sample - the 50.17% ROI there is noise. No difference tests run, nothing here would clear significance at these sample sizes.