import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option("display.width", None)
pd.set_option("display.max_columns", None)
df = pd.read_csv("clean_bets.csv")
df["date"] = pd.to_datetime(df["date"])
df = df[ df["CL"].notna()]
df = df[~df["Fixture"].isin(["Double", "Treble", "Acca", "4 Fold", "6 Fold"])]
df["clv"] = (df["Odds"] / df["CL"] - 1) * 100
print(len(df))
low = df[df["clv"] <= 10.615]
high = df[df["clv"] > 10.615]
print(df["clv"].describe())
df["clv_bucket"] = pd.qcut(df["clv"], 2)
print(df["clv_bucket"].value_counts())
buckets = df.groupby("clv_bucket").agg({"Unit Stake": "sum", "Profit": "sum", "Bet": "count", "clv": "mean", "Odds": "mean"})
buckets["roi"] = buckets["Profit"]/buckets["Unit Stake"]* 100
print(buckets)
diffs = []
for i in range(10000):
    a = high.sample(n=661, replace=True)
    b = low.sample(n=665, replace=True)
    roi_a = a["Profit"].sum() / a["Unit Stake"].sum() * 100
    roi_b = b["Profit"].sum() / b["Unit Stake"].sum() * 100
    diffs.append(roi_a - roi_b)
print(np.mean(diffs))
print(np.percentile(diffs, 2.5))
print(np.percentile(diffs, 97.5))