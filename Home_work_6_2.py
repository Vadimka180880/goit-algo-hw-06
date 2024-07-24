import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (райони)
nodes = ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]
G.add_nodes_from(nodes)

# Додавання ребер (дороги між районами)
edges = [("Manhattan", "Brooklyn"), ("Manhattan", "Queens"), ("Manhattan", "Bronx"),
         ("Brooklyn", "Queens"), ("Brooklyn", "Bronx"), ("Brooklyn", "Staten Island"),
         ("Queens", "Bronx")]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_color="black")
plt.title("Транспортна мережа районів Нью-Йорка")
plt.show()

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

print("DFS знайдені шляхи:")
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
