import geopandas as gpd
import matplotlib.pyplot as plt

india = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
tamilnadu = india[india['name'] == 'India']
tamilnadu.plot(color='lightgrey', edgecolor='black')
plt.title('Tamil Nadu Cities Population Visualization (Sample)')
plt.show()
