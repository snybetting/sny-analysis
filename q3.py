import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("clean_bets.csv")
print(df.shape)
df["date"] = pd.to_datetime(df["date"])
print(df.dtypes)
monthly = df.groupby(df["date"].dt.to_period("M")).agg({"Unit Stake": "sum", "Profit": "sum", "Bet": "count"})
monthly["roi"] = monthly["Profit"]/monthly["Unit Stake"]* 100
print(monthly)
june25 = df[(df["date"] >= "2025-06-01") & (df["date"] < "2025-07-01")]
june26 = df[(df["date"] >= "2026-06-01") & (df["date"] < "2026-07-01")]
print(june25["League"].value_counts())
print(june26["League"].value_counts())