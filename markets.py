import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("clean_bets.csv")
df["date"] = pd.to_datetime(df["date"])
df["market"] = "other"
df.loc[df["Bet"].str.contains("Corner"), "market"] = "corners"
df.loc[df["Bet"].str.contains("Card"), "market"] = "cards"
df.loc[df["Bet"].str.contains("Booking"), "market"] = "cards"
print(df["market"].value_counts())
markets = df.groupby("market").agg({"Unit Stake": "sum", "Profit": "sum", "Bet": "count"})
markets["roi"] = markets["Profit"]/markets["Unit Stake"]* 100
print(markets)
df["season"] = "24/25"
df.loc[df["date"] >= "2025-08-01", "season"] = "25/26"
seasons = df.groupby(["market", "season"]).agg({"Unit Stake": "sum", "Profit": "sum", "Bet": "count"})
seasons["roi"] = seasons["Profit"]/seasons["Unit Stake"]* 100
print(seasons)
df = df[ df["CL"].notna()]
df = df[~df["Fixture"].isin(["Double", "Treble", "Acca", "4 Fold", "6 Fold"])]
df["clv"] = (df["Odds"] / df["CL"] - 1) * 100
clv_split = df.groupby(["market", "season"]).agg({"clv": "mean", "Bet": "count"})
print(clv_split)