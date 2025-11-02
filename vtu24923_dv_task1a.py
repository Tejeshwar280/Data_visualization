import pandas as pd
import numpy as np

a = pd.read_csv("/content/student.csv")
print(a)
print(a.shape)
a.info()
print(a.describe())
print(a.head())
print(pd.isna(a).sum())
a = a.dropna()
a = a.drop_duplicates()
print(a)
