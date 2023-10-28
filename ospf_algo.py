import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random

# Define a graph representing the network topology
graph = {
    'A': {'B': random.randint(1, 10), 'C': random.randint(1, 10)},
    'B': {'A': random.randint(1, 10), 'C': random.randint(1, 10), 'D': random.randint(1, 10)},
    'C': {'A': random.randint(1, 10), 'B': random.randint(1, 10), 'D': random.randint(1, 10)},
    'D': {'B': random.randint(1, 10), 'C': random.randint(1, 10)}
}

# Implement the OSPF algorithm
def ospf(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Create a networkx graph for visualization
G = nx.Graph()
for node, neighbors in graph.items():
    G.add_node(node)
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Example usage
source_node = 'A'
shortest_distances = ospf(graph, source_node)

# Visualization
pos = nx.spring_layout(G)  # Layout for visualization
labels = {node: f"{node}\n({shortest_distances[node]})" for node in G.nodes()}

edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}

# Find the shortest path
shortest_path_edges = [(source_node, node) for node in G.nodes() if node != source_node and shortest_distances[node] != float('inf')]

# Draw arrows on the edges to represent OSPF paths
edges = nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1.0, alpha=0.5, arrows=True, edge_color='k')

# Highlight the nodes of the shortest path
shortest_path_nodes = [source_node] + [node for node in G.nodes() if node != source_node and shortest_distances[node] != float('inf')]
node_colors = ['red' if node in shortest_path_nodes else 'lightblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_color=node_colors)

nx.draw(G, pos, with_labels=True, labels=labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
for node, distance in shortest_distances.items():
    print(f'Shortest distance from {source_node} to {node} is {distance}')