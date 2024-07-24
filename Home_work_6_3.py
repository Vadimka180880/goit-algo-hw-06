import heapq
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

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    shortest_path_tree = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Перевірка всіх сусідніх вершин
        for neighbor, data in graph[current_node].items():
            weight = data['weight']
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_node

    return distances, shortest_path_tree

# Функція для побудови шляху від початкового до кінцевого вузла
def get_path(tree, start, goal):
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = tree[node]
    path.append(start)
    path.reverse()
    return path

# Виконання алгоритму Дейкстри для кожної вершини
all_pairs_shortest_paths = {}
for start_node in G.nodes:
    distances, tree = dijkstra(G, start_node)
    all_pairs_shortest_paths[start_node] = {end_node: get_path(tree, start_node, end_node) for end_node in G.nodes if end_node in tree}

# Виведення результатів
print("Найкоротші шляхи між всіма вершинами графа:")
for start, paths in all_pairs_shortest_paths.items():
    for end, path in paths.items():
        print(f"Найкоротший шлях від {start} до {end}: {path}")

print("\nДовжина найкоротших шляхів між всіма вершинами графа:")
for start_node, distances in distances.items():
    print(f"Довжина найкоротшого шляху від {start_node}:")
    for end_node, distance in distances.items():
        print(f"  до {end_node}: {distance}")
