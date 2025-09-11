import pandas as pd
import numpy as np

df = pd.read_csv(
    r"C:\Users\rajpu\OneDrive\Desktop\Mayuri Course\Assignment3\sales_data.csv"
)
print(df.head())

col = df.columns
print("columns are:", col)

NullValues = df.isnull().sum()
print("Null values are:", NullValues)


df["Revenue"] = df["Order_Quantity"] * df["Unit_Price"]
total_revenue = df["Revenue"].sum()

print("Total Revenue:", total_revenue)
