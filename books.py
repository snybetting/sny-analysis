import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("clean_bets.csv")
df["date"] = pd.to_datetime(df["date"])
df = df[df["CL"].notna()]
df = df[~df["Fixture"].isin(["Double", "Treble", "Acca", "4 Fold", "6 Fold"])]
df["clv"] = (df["Odds"] / df["CL"] - 1) * 100
df["season"] = "24/25"
df.loc[df["date"] >= "2025-08-01", "season"] = "25/26"
print(df["Bookmaker"].value_counts())
df["book"] = df["Bookmaker"].replace({
    "Bet35": "Bet365",
    "Paddy Power": "Flutter",
    "Sky Bet": "Flutter"
})
df = df[df["book"].isin(["Bet365", "Flutter"])]
print(df["book"].value_counts())
books = df.groupby("book").agg({"clv": "mean", "Unit Stake": "sum", "Profit": "sum", "Bet": "count", "Odds": "mean"})
books["roi"] = books["Profit"]/books["Unit Stake"]* 100
print(books)
by_season = df.groupby(["book", "season"]).agg({"clv": "mean", "Unit Stake": "sum", "Profit": "sum", "Bet": "count", "Odds": "mean"})
by_season["roi"] = by_season["Profit"]/by_season["Unit Stake"]* 100
print(by_season)
full = pd.read_csv("clean_bets.csv")
full["date"] = pd.to_datetime(full["date"])
full = full[~full["Fixture"].isin(["Double", "Treble", "Acca", "4 Fold", "6 Fold"])]
full["season"] = "24/25"
full.loc[full["date"] >= "2025-08-01", "season"] = "25/26"
full["book"] = full["Bookmaker"].replace({
    "Bet35": "Bet365",
    "Paddy Power": "Flutter",
    "Sky Bet": "Flutter"
})
full = full[full["book"].isin(["Bet365", "Flutter"])]
full_season = full.groupby(["book", "season"]).agg({"Unit Stake": "sum", "Profit": "sum", "Bet": "count", "Odds": "mean"})
full_season["roi"] = full_season["Profit"]/full_season["Unit Stake"]* 100
print(full_season)