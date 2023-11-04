import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph (DiGraph) to represent the network topology
G = nx.DiGraph()

# Add nodes for devices (source, routers, destination) and specify MAC addresses
nodes = {
    "Source": "00:11:22:33:44:55",
    "Router1": "11:22:33:44:55:66",
    "Router2": "22:33:44:55:66:77",
    "Router3": "33:44:55:66:77:88",
    "Destination": "44:55:66:77:88:99",
}
G.add_nodes_from(nodes.keys())

# Define edges to represent connections and specify MAC addresses as attributes
edges = [
    ("Source", "Router1", {"label": f"{nodes['Source']} to {nodes['Router1']}"}),
    ("Router1", "Router2", {"label": f"{nodes['Router1']} to {nodes['Router2']}"}),
    ("Router2", "Router3", {"label": f"{nodes['Router2']} to {nodes['Router3']}"}),
    ("Router3", "Destination", {"label": f"{nodes['Router3']} to {nodes['Destination']}"}),
]
G.add_edges_from(edges)

# Position the nodes for visualization
pos = nx.spring_layout(G)

# Draw the network topology
nx.draw(G, pos, with_labels=False, node_size=800, node_color="skyblue")

# Add edge labels (including MAC addresses)
edge_labels = {(u, v): data["label"] for u, v, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color="black")

# Annotate the visualization
plt.title("End-to-End Packet Forwarding")

# Show the plot
plt.show()
