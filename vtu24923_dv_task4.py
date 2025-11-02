import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

df = pd.read_csv("/content/archive (4).zip")
sns.pairplot(df[['Age','Debt','YearsEmployed']])
plt.show()

fig = px.parallel_coordinates(df, color="Approved", dimensions=["Age","Debt","CreditScore"])
fig.show()

subset = df.head(20)
plt.plot(subset['Age'], subset['Debt'], label='Debt')
plt.plot(subset['Age'], subset['CreditScore'], label='Credit Score')
plt.legend()
plt.show()

grouped = subset.groupby('Age')[['Debt','CreditScore']].sum()
grouped.plot(kind='bar', stacked=True)
plt.show()
