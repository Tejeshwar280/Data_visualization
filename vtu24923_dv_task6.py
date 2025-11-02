import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

G = nx.Graph()
df_nodes = pd.read_csv('stack_network_nodes.csv')
df_links = pd.read_csv('stack_network_links.csv')

for _, r in df_nodes.iterrows():
    G.add_node(r['name'], group=r['group'], size=r['nodesize'])
for _, r in df_links.iterrows():
    G.add_edge(r['source'], r['target'], weight=r['value'])

plt.figure(figsize=(15,15))
nx.draw(G, with_labels=True, node_size=300, edge_color='lightgray')
plt.show()
