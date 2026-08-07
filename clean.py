import pandas as pd
df = pd.read_csv("Full History Pinn Devig - Pinnacle Corners + Cards.csv", skiprows=9)
print(df.shape)
print(df.columns.tolist())
print (df.head(15))
print (df.dtypes)
df["Date"] = df["Date"].ffill()
df["Unnamed: 0"] = df["Unnamed: 0"].ffill()
df = df[ df["Unit Stake"].notna()]
print(df.shape)
print(df.head(15))
df["date"] = pd.to_datetime(df["Date"]+"/"+df["Unnamed: 0"], format="%d/%m/%Y")
print(df["date"].head(15))
assert len(df) == 2600
assert round( df["Profit"].sum() , 2)== 311.36
assert round( df["Unit Stake"].sum() , 2)== 3008.88
df["EV%"] = pd.to_numeric( df["EV%"].str.replace("%", "") , errors="coerce")
df["CL"] = pd.to_numeric( df["CL"], errors="coerce")
print(df.dtypes)
df.to_csv("clean_bets.csv", index=False)