import networkx as nx
import matplotlib.pyplot as plt

# Create a graph for the STP topology
G = nx.Graph()
G.add_node("Root Bridge")
G.add_node("Bridge 1")
G.add_node("Bridge 2")
G.add_edge("Root Bridge", "Bridge 1")
G.add_edge("Root Bridge", "Bridge 2")

# Specify bridge roles (root, designated, etc.) as node attributes

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=5000, node_color='skyblue')
plt.show()
