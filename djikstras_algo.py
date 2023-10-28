import networkx as nx
import matplotlib.pyplot as plt
import random

# Function to visualize the graph
def visualize_graph(G, pos, node_colors, edge_colors):
    plt.figure(figsize=(10, 6))
    
    # Draw nodes
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=700, font_size=12, font_color='white')
    
    # Draw edges
    edges = G.edges()
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_colors)
    
    plt.axis('off')
    plt.show()

# Dijkstra's algorithm to find the shortest path
def dijkstra(G, source, target):
    # Initialize distances and predecessors
    distances = {node: float('inf') for node in G.nodes()}
    predecessors = {node: None for node in G.nodes()}
    distances[source] = 0
    
    # Priority queue for selecting the next node
    unvisited_nodes = list(G.nodes())
    
    while unvisited_nodes:
        # Select the node with the shortest distance
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        unvisited_nodes.remove(current_node)
        
        for neighbor in G.neighbors(current_node):
            tentative_distance = distances[current_node] + G[current_node][neighbor]['weight']
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                predecessors[neighbor] = current_node
        
        if current_node == target:
            break
    
    # Construct the shortest path
    path = []
    while predecessors[target]:
        path.insert(0, target)
        target = predecessors[target]
    path.insert(0, source)
    
    return path

# Create a sample graph
G = nx.Graph()
G.add_edge('A', 'B', weight=random.randint(1, 10))
G.add_edge('A', 'C', weight=random.randint(1, 10))
G.add_edge('B', 'C', weight=random.randint(1, 10))
G.add_edge('B', 'D', weight=random.randint(1, 10))
G.add_edge('C', 'D', weight=random.randint(1, 10))
G.add_edge('C', 'E', weight=random.randint(1, 10))
G.add_edge('D', 'E', weight=random.randint(1, 10))

# Define the source and target nodes
source_node = 'A'
target_node = 'E'

# Find the shortest path
shortest_path = dijkstra(G, source_node, target_node)

# Color nodes and edges for visualization
node_colors = ['lightblue' if node in shortest_path else 'lightgray' for node in G.nodes()]
edge_colors = ['blue' if (u, v) in shortest_path or (v, u) in shortest_path else 'gray' for u, v in G.edges()]

# Position for visualizing the graph
pos = nx.spring_layout(G)

# Visualize the graph and the shortest path
visualize_graph(G, pos, node_colors, edge_colors)

print("Shortest Path:", shortest_path)
