import pandas as pd


df = pd.read_csv("experience.csv")


print("Full DataFrame:\n")
print(df)


rows, cols = df.shape
print("\nNumber of rows:", rows)
print("Number of columns:", cols)


print("\nLength of DataFrame:", len(df))


print("\nFirst 2 rows:\n")
print(df.head(2))
