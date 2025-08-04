import pandas as pd

# Load raw CSV
df = pd.read_csv("P:/Data Tools/Datasets/NVIDIA_STOCK.csv", header=0)

# Fix headers and drop garbage rows
df.columns = ["date"] + df.columns.tolist()[1:]
df.drop(index=[1, 2], inplace=True)
df.columns = [str(col).strip().lower().replace(" ", "_") for col in df.columns]

# Convert data types
df["date"] = pd.to_datetime(df["date"], errors="coerce")
for col in df.columns:
    if col != "date":
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Final cleanup
df.dropna(inplace=True)
df.sort_values("date", inplace=True)
df.reset_index(drop=True, inplace=True)

# Export cleaned CSV for SQL
df.to_csv("P:/Data Tools/Datasets/NVIDIA_STOCK_cleaned.csv", index=False)
