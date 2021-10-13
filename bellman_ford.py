import math
from graph import Graph

def bellman_ford(graph, s):
  distance = {}
  predecessor = {}

  for v in graph._nodes:
    distance[v] = math.inf
    predecessor[v] = None

  distance[s] = 0
  edges = graph.get_edges()

  for i in range(len(graph.get_nodes())-1):
    for (u, v, w) in edges:
      if distance[v] > (distance[u] + w):
        distance[v] = distance[u] + w
        predecessor[v] = u

  for (u, v, w) in edges:
    if distance[v] > (distance[u] + w):
      print("Negative cycle")
      return False
  return True
