import pandas as pd
import numpy as np
df = pd.read_csv("clean_bets.csv")
print(df["Odds"].describe())
print((df["Odds"] > 10).sum())
print(df[df["Odds"] > 10]["Odds"].describe())
print(df[df["Odds"] > 10]["Profit"].sum())
df["p"] = 1.10 / df["Odds"]
print(df["p"].describe())
for N in [1000, 2600, 5000, 10000, 20000, 50000]:
    rois = []
    for i in range(2000):
        odds = df["Odds"].sample(n=N, replace=True).values
        p = 1.10 / odds
        wins = np.random.random(N) < p
        returns = np.where(wins, odds - 1, -1)
        rois.append(returns.sum() / N * 100)
    print(N, round(np.percentile(rois, 2.5), 2), round(np.percentile(rois, 97.5), 2))