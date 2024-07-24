import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (райони)
nodes = ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]
G.add_nodes_from(nodes)

# Додавання ребер з вагами (дороги між районами)
edges = [
    ("Manhattan", "Brooklyn", 5), 
    ("Manhattan", "Queens", 7), 
    ("Manhattan", "Bronx", 10),
    ("Brooklyn", "Queens", 3), 
    ("Brooklyn", "Bronx", 8), 
    ("Brooklyn", "Staten Island", 12),
    ("Queens", "Bronx", 6)
]
G.add_weighted_edges_from(edges)

# Візуалізація графа з вагами ребер
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Визначення позицій для вузлів
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_color="black")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа районів Нью-Йорка з вагами ребер")
plt.show()

# Алгоритм Дейкстри для знаходження найкоротших шляхів
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

print("Найкоротші шляхи між всіма вершинами графа:")
for start, paths in shortest_paths.items():
    for end, path in paths.items():
        print(f"Найкоротший шлях від {start} до {end}: {path}")

# Дістанція (вага) найкоротших шляхів
shortest_paths_lengths = dict(nx.all_pairs_dijkstra_path_length(G))

print("\nДовжина найкоротших шляхів між всіма вершинами графа:")
for start, lengths in shortest_paths_lengths.items():
    for end, length in lengths.items():
        print(f"Довжина найкоротшого шляху від {start} до {end}: {length}")
