import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("clean_bets.csv")
df["date"] = pd.to_datetime(df["date"])
df = df[ df["CL"].notna()]
df["clv"] = (df["Odds"] / df["CL"] - 1) * 100
print(np.mean(df["clv"]))
print(np.median(df["clv"]))
print(len(df))
s2425 = df[df["date"] < "2025-08-01"]
s2526 = df[df["date"] >= "2025-08-01"]
print(len(s2425))
print(len(s2526))
print(np.mean(s2425["clv"]))
print(np.mean(s2526["clv"]))
clv_diffs = []
for i in range(10000):
    a = s2425.sample(n=750, replace=True)
    b = s2526.sample(n=614, replace=True)
    clv_a = a["clv"].mean()
    clv_b = b["clv"].mean()
    clv_diffs.append(clv_a - clv_b)
print(np.mean(clv_diffs))
print(np.percentile(clv_diffs, 2.5))
print(np.percentile(clv_diffs, 97.5))