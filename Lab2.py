import networkx as nx
import matplotlib.pyplot as plt

# Graph build
star = nx.star_graph(15)
path = nx.path_graph(10)
G = nx.disjoint_union(star, path)
G.add_edge(0, 16)

star = nx.star_graph(23)
G = nx.disjoint_union(G, star)
G.add_edge(25, 26)

# Centrality
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print("c(", n, ")=", centrality[n])

# Draw
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True)
plt.show()