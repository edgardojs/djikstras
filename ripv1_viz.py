import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph (DiGraph) to represent the network topology
G = nx.DiGraph()

# Add nodes (routers) to the network
G.add_node("Router1")
G.add_node("Router2")
G.add_node("Router3")

# Add edges (links between routers)
G.add_edge("Router1", "Router2")
G.add_edge("Router2", "Router3")

# Draw the network topology
pos = nx.spring_layout(G, seed=42)  # Layout algorithm (you can change this)
nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")
labels = nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, edge_color="gray")

# Show the plot
plt.show()