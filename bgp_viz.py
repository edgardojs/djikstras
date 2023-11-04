import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph (DiGraph) to represent the BGP network
G = nx.DiGraph()

# Add Autonomous Systems (ASes) as nodes
G.add_node("AS1")
G.add_node("AS2")
G.add_node("AS3")

# Add BGP peer relationships (edges)
G.add_edge("AS1", "AS2", label="Peer")
G.add_edge("AS2", "AS3", label="Peer")

# Set positions for the ASes (you can customize this)
pos = {"AS1": (0, 0), "AS2": (1, 0), "AS3": (2, 0)}

# Draw the BGP network topology
edge_labels = {(u, v): d["label"] for u, v, d in G.edges(data=True)}
nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, edge_color="gray")

# Show the plot
plt.show()