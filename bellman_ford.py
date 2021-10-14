import math


def bellman_ford(graph, s):
    distances = {}
    predecessors = {}

    for v in graph.get_nodes():
        distances[v] = math.inf
        predecessors[v] = None

    distances[s] = 0
    edges = graph.get_edges()

    for i in range(len(graph.get_nodes()) - 1):
        for (u, v, w) in edges:
            if distances[v] > (distances[u] + w):
                distances[v] = distances[u] + w
                predecessors[v] = u

    for (u, v, w) in edges:
        if distances[v] > (distances[u] + w):
            raise RuntimeError("Negative cycle")

    return distances
