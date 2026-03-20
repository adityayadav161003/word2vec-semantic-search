import pandas as pd

df = pd.read_csv("../data/FA-KES-Dataset.csv", encoding='latin1')

print("First 5 rows:\n")
print(df.head())

print("\nColumns:\n")
print(df.columns)