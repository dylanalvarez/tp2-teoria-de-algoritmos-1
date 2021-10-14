import copy

from graph import Graph
from bellman_ford import bellman_ford
from dijkstra import dijkstra

EXTRA_NODE_KEY = "@"
EXTRA_NODE_WEIGHT = 0


def johnson(graph):
    # step 1
    johnson_graph = _graph_with_extra_node(graph)

    # step 2
    distances = bellman_ford(johnson_graph, EXTRA_NODE_KEY)

    # step 3
    bellman_ford_graph = _graph_from_bellman_ford(graph, distances)

    # step 4
    result = {}
    for u in bellman_ford_graph.get_nodes():
        min_paths = dijkstra(bellman_ford_graph, u)
        result[u] = min_paths
    return result


def _graph_with_extra_node(graph):
    johnson_graph = copy.deepcopy(graph)
    for a in johnson_graph.get_nodes():
        johnson_graph.add_edge(EXTRA_NODE_KEY, a, EXTRA_NODE_WEIGHT)
    return johnson_graph


def _graph_from_bellman_ford(graph, distances):
    bellman_ford_graph = Graph()

    for (u, v, w) in graph.get_edges():
        new_weight = w + distances[u] - distances[v]
        bellman_ford_graph.add_edge(u, v, new_weight)

    return bellman_ford_graph

