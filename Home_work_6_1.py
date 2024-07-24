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

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"Район {node}: ступінь {degree}")
