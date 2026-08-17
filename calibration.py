import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("clean_bets.csv")
df["date"] = pd.to_datetime(df["date"])
df = df[~df["Fixture"].isin(["Double", "Treble", "Acca", "4 Fold", "6 Fold"])]
df = df[df["EV%"].notna()]
print(len(df))
print(df["EV%"].mean())
print(df["Profit"].sum() / df["Unit Stake"].sum() * 100)
df["ev_bucket"] = pd.cut(df["EV%"], bins=[100, 105, 110, 115, 120, 200])
print(df["ev_bucket"].value_counts())
buckets = df.groupby("ev_bucket").agg({"Unit Stake": "sum", "Profit": "sum", "Bet": "count", "EV%": "mean"})
buckets["roi"] = buckets["Profit"]/buckets["Unit Stake"]* 100
buckets["claimed"] = buckets["EV%"] - 100
print(buckets)
top = df[df["EV%"] > 120]
print(len(top))
top_rois = []
for i in range(10000):
     a = top.sample(n=110, replace=True)
     roi = a["Profit"].sum() / a["Unit Stake"].sum() * 100
     top_rois.append(roi)
print(np.mean(top_rois))
print(np.percentile(top_rois, 2.5))
print(np.percentile(top_rois, 97.5))
bounds = []
for b in buckets.index:
    sub = df[df["ev_bucket"] == b]
    rois = []
    for i in range(2000):
        a = sub.sample(n=len(sub), replace=True)
        rois.append(a["Profit"].sum() / a["Unit Stake"].sum() * 100)
    bounds.append([np.percentile(rois, 2.5), np.percentile(rois, 97.5)])
lower = buckets["roi"] - [b[0] for b in bounds]
upper = [b[1] for b in bounds] - buckets["roi"]
plt.errorbar(buckets["claimed"], buckets["roi"], yerr=[lower, upper], fmt="o")
plt.plot([0, 30], [0, 30])
plt.xlabel("Claimed EV %")
plt.ylabel("Realised ROI %")
print(bounds)
plt.show()
