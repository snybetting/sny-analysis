import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("clean_bets.csv")
df["date"] = pd.to_datetime(df["date"])
df["line"] = df["Bet"].str.extract(r"(\d+\.?\d*)").astype(float)
safe = df[(df["line"] % 1 == 0.5) | (df["line"].isna())]
print(df["line"].head(20))
print(df["Bet"].head(20))
print(len(safe))
print(safe["Profit"].sum() / safe["Unit Stake"].sum() * 100)
diffs = []
for i in range(10000):
     a = safe.sample(n=1559, replace=True)
     roi_a = a["Profit"].sum() / a["Unit Stake"].sum() * 100
     diffs.append(roi_a)
print(np.mean(diffs))
print(np.percentile(diffs, 2.5))
print(np.percentile(diffs, 97.5))