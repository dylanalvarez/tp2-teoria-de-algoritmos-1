import math
from heapq import heappush, heappop


def dijkstra(graph, s):
    h = []
    distances = {}
    parents = {}
    seen = {}

    for u in graph.get_nodes():
        distances[u] = math.inf
        parents[u] = None
        seen[u] = False
    distances[s] = 0
    heappush(h, (distances[s], s))

    while len(h):
        u = heappop(h)[1]
        seen[u] = True
        for v in graph.get_all_adjacent(u):
            if seen[v]:
                continue
            if distances[v] > (distances[u] + graph.get_weight(u, v)):
                distances[v] = distances[u] + graph.get_weight(u, v)
                parents[v] = u
                heappush(h, (distances[v], v))
    return distances
