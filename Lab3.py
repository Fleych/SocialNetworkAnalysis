import networkx as nx

# Graph build
n = 60
p = 0.45
G = nx.erdos_renyi_graph(n, p)

# Average degree
sum_degree = 0
for n in G.nodes():
  sum_degree = sum_degree + G.degree(n)
avg_degree_1 = float(sum_degree) / n

avg_degree_2 = (n - 1) * p

print(f"avg_degree_1 = {avg_degree_1}, avg_degree_2 = {avg_degree_2}")