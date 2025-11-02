import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/content/Employee.csv")
df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
plt.title('Gender Distribution')
plt.show()

plt.hist(df['Age'], bins=10, edgecolor='black')
plt.title('Age Distribution')
plt.show()

sns.kdeplot(df['Age'], fill=True)
plt.title('Density Plot of Age')
plt.show()

sns.rugplot(df['JoiningYear'])
plt.title('Rug Plot of Joining Year')
plt.show()
