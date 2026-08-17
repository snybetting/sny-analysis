import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("clean_bets.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")
df["unit_profit"] = (df["Profit"] / df["Unit Stake"])
df["cumulative"] = df["unit_profit"].cumsum()
print(df["cumulative"].iloc[-1])
df["peak"] = df["cumulative"].cummax()
df["drawdown"] = df["cumulative"] - df["peak"]
print(df["drawdown"].min())
trough = df["drawdown"].idxmin()
print(df.loc[trough, "date"])
peak_value = df.loc[trough, "peak"]
peak_row = df[df["cumulative"] >= peak_value].index[0]
print(df.loc[peak_row, "date"])
after = df.loc[trough:]
recovery = after[after["cumulative"] >= peak_value]
print(recovery["date"].iloc[0])
plt.plot(df["date"], df["cumulative"])
plt.ylabel("Cumulative profit (units, 1u flat)")
plt.title("SNY equity curve, Aug 2024 - Jul 2026")
plt.figure()
plt.plot(df["date"], df["drawdown"])
plt.ylabel("Drawdown (units)")
plt.title("Drawdown from running peak")
plt.show()