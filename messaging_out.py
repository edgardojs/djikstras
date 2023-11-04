import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph (DiGraph) to represent the network topology
G = nx.DiGraph()

# Add nodes for PC1, PC2, and three routers (R1, R2, R3)
nodes = ["PC1", "R1", "R2", "R3", "PC2"]
G.add_nodes_from(nodes)

# Add edges to represent the connections
edges = [("PC1", "R1"), ("R1", "R2"), ("R2", "R3"), ("R3", "PC2")]
G.add_edges_from(edges)

# Position the nodes for visualization
pos = nx.spring_layout(G)

# Draw the network topology
nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")
edge_labels = {(u, v): f"{u} to {v}" for u, v in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Simulate ARP and packet forwarding
def simulate_communication(source, destination):
    print(f"PC1 sends a packet to {source}")
    print(f"ARP Request from PC1 to {source}: Who has {source}'s MAC address?")
    print(f"ARP Reply from {source} to PC1: My MAC address is <MAC of {source}>")
    print(f"PC1 encapsulates the packet with the MAC address of {source} and sends it to {source}")
    print(f"{source} receives the packet")

    if source != destination:
        next_hop = nx.shortest_path(G, source=source, target=destination)[1]
        simulate_communication(next_hop, destination)

simulate_communication("PC1", "PC2")

# Show the plot
plt.show()
