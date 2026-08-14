import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("clean_bets.csv")
print(df.shape)
results = []
for i in range(10000):
    s = df.sample(n=2600, replace=True)
    results.append(s["Profit"].sum()/s["Unit Stake"].sum()* 100)
print(len(results))
print(np.mean(results))
print(np.percentile(results, 2.5))
print(np.percentile(results, 97.5))
df["date"] = pd.to_datetime(df["date"])
s2425 = df[df["date"] < "2025-08-01"]
s2526 = df[df["date"] >= "2025-08-01"]
print(len(s2425))
print(len(s2526))
results2425 = []
for i in range(10000):
    s = s2425.sample(n=1191, replace=True)
    results2425.append(s["Profit"].sum() / s["Unit Stake"].sum() * 100)
results2526 = []
for i in range(10000):
    s = s2526.sample(n=1409, replace=True)
    results2526.append(s["Profit"].sum() / s["Unit Stake"].sum() * 100)
print(np.mean(results2425))
print(np.percentile(results2425, 2.5))
print(np.percentile(results2425, 97.5))
print(np.mean(results2526))
print(np.percentile(results2526, 2.5))
print(np.percentile(results2526, 97.5))
diffs = []
for i in range(10000):
    a = s2425.sample(n=1191, replace=True)
    b = s2526.sample(n=1409, replace=True)
    roi_a = a["Profit"].sum() / a["Unit Stake"].sum() * 100
    roi_b = b["Profit"].sum() / b["Unit Stake"].sum() * 100
    diffs.append(roi_a - roi_b)
print(np.mean(diffs))
print(np.percentile(diffs, 2.5))
print(np.percentile(diffs, 97.5))