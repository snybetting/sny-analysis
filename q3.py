import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("clean_bets.csv")
print(df.shape)
df["date"] = pd.to_datetime(df["date"])
print(df.dtypes)
monthly = df.groupby(df["date"].dt.to_period("M")).agg({"Unit Stake": "sum", "Profit": "sum", "Bet": "count"})
monthly["roi"] = monthly["Profit"]/monthly["Unit Stake"]* 100
monthly["roi"].plot()
plt.ylabel("ROI")
plt.figure()
monthly["Bet"].plot()
plt.ylabel("Bets")
plt.show()
print(monthly)