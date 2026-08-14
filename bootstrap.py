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