import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/content/student_alcohol.csv")
sns.kdeplot(data=df, x='Income', hue='Ethnicity', fill=True)
plt.title('Income Distribution by Ethnicity')
plt.show()

sns.boxplot(x='Citizen', y='Income', data=df)
sns.violinplot(x='Ethnicity', y='Income', data=df)
plt.show()

sns.lmplot(data=df, x='Age', y='Income', line_kws={'color': 'red'})
plt.title('Scatter Plot with Fit Line')
plt.show()
