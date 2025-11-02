import pandas as pd

df = pd.read_csv("/content/sample_kaggle_dataset.csv")
print(df.head())
print(df.isnull().sum())
df = df.dropna()
df = df.drop_duplicates()
print(df.shape)
