import pandas as pd
import glob

files = glob.glob("data/*.csv")

df_list = []

for file in files:
    df = pd.read_csv(file)

    # Filter Pink Morsel
    df = df[df["product"] == "pink morsel"]

    # Only CLEAN price (NOT quantity)
    df["price"] = df["price"].astype(str).str.replace("$", "", regex=False)

    # Convert to numeric
    df["price"] = pd.to_numeric(df["price"])
    df["quantity"] = pd.to_numeric(df["quantity"])

    # Compute sales properly
    df["sales"] = df["quantity"] * df["price"]

    # Convert date
    df["date"] = pd.to_datetime(df["date"])

    # Keep required columns
    df = df[["sales", "date", "region"]]

    df_list.append(df)

final_df = pd.concat(df_list, ignore_index=True)

final_df.to_csv("processed_sales.csv", index=False)

print(final_df.head())
print("Done! File saved as processed_sales.csv")