import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/content/sentimentdataset.csv")
platform_likes = df.groupby('Platform')['Likes'].sum().head(5)
plt.figure(figsize=(4,4))
platform_likes.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Top Platforms by Likes')
plt.show()

top_countries = df.nlargest(5, 'Likes')
plt.bar(top_countries['Country'], top_countries['Likes'], color='skyblue')
plt.title('Top Countries by Likes')
plt.show()

sns.scatterplot(data=df, x='Retweets', y='Likes', color='blue')
plt.title('Scatter Plot of Retweets vs Likes')
plt.show()
