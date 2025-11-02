import squarify
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("/content/USA_cars_datasets.csv")
brand_price = df.groupby('brand')['price'].sum().reset_index()
squarify.plot(sizes=brand_price['price'], label=brand_price['brand'], alpha=0.7)
plt.title("Tree Map of Total Price by Brand")
plt.axis('off')
plt.show()

sunburst_data = df.groupby(['brand','model'])['price'].sum().reset_index()
fig = px.sunburst(sunburst_data, path=['brand','model'], values='price')
fig.show()
