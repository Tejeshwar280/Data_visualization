import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv('/content/testset.csv')
data['datetime_utc'] = pd.to_datetime(data['datetime_utc'])
sns.lineplot(data=data, x='datetime_utc', y='_tempm')
plt.title('Temperature Over Time')
plt.show()

x = np.arange(len(data)).reshape(-1,1)
y = data['_tempm'].fillna(method='ffill').values
model = LinearRegression().fit(x, y)
plt.scatter(x, y, color='blue')
plt.plot(x, model.predict(x), color='red')
plt.title('Trend Line for Temperature')
plt.show()
