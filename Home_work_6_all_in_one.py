import networkx as nx
import matplotlib.pyplot as plt

# Завдання 1
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

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"Район {node}: ступінь {degree}")

# Завдання 2
# Алгоритм DFS для знаходження шляху
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Алгоритм BFS для знаходження шляху
def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Знаходження шляхів між Manhattan і Staten Island
start = "Manhattan"
goal = "Staten Island"

dfs_paths = list(dfs_path(G, start, goal))
bfs_paths = list(bfs_path(G, start, goal))

print("\nDFS знайдені шляхи:")
for path in dfs_paths:
    print(path)

print("\nBFS знайдені шляхи:")
for path in bfs_paths:
    print(path)

# Аналіз результатів
print("\nАналіз шляхів:")
print(f"Кількість шляхів знайдених DFS: {len(dfs_paths)}")
print(f"Кількість шляхів знайдених BFS: {len(bfs_paths)}")
print("\nПояснення різниці в шляхах:")
print("DFS шукає глибше перед тим, як перемикатися на інше відгалуження, що може призвести до більш довгих або менш оптимальних шляхів.")
print("BFS шукає ширше, перевіряючи всі сусідні вершини на кожному рівні перед тим, як перейти до наступного рівня, що зазвичай призводить до більш коротких шляхів.")

# Завдання 3
# Алгоритм Дейкстри для знаходження найкоротших шляхів
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

print("\nНайкоротші шляхи між всіма вершинами графа:")
for start, paths in shortest_paths.items():
    for end, path in paths.items():
        print(f"Найкоротший шлях від {start} до {end}: {path}")

# Дістанція (вага) найкоротших шляхів
shortest_paths_lengths = dict(nx.all_pairs_dijkstra_path_length(G))

print("\nДовжина найкоротших шляхів між всіма вершинами графа:")
for start, lengths in shortest_paths_lengths.items():
    for end, length in lengths.items():
        print(f"Довжина найкоротшого шляху від {start} до {end}: {length}")
