import copy

from graph import Graph
from bellman_ford import bellman_ford
from dijkstra import dijkstra

EXTRA_NODE_KEY = "@"
EXTRA_NODE_WEIGHT = 0


def johnson(graph):
    """
    Algoritmo de Johnson
    Genera los caminos mínimos entre todos los pares de nodos de {graph}
    Permite aristas de peso negativos, pero no permite ciclos de coste total negativo
    """

    # step 1
    johnson_graph = _graph_with_extra_node(graph)

    # step 2
    # Se utiliza Bellman Ford utilizando el nuevo vértice adicional
    distances = bellman_ford(johnson_graph, EXTRA_NODE_KEY)

    # step 3
    # Se genera un nuevo grafo intercambiando los pesos del grafo original 
    # por la fórmula {weight + distancia(u) - distancia (v)}
    bellman_ford_graph = _graph_from_bellman_ford(graph, distances)

    # step 4
    # Se utiliza Dijkstra para encontrar caminos mínimos entre todos los pares de nodos de {graph}
    # es posible utilizar Dijkstra ya que se trata de un caso menos general en que todas las aristas
    # tienen peso no negativo
    result = {}
    for u in bellman_ford_graph.get_nodes():
        min_paths = dijkstra(bellman_ford_graph, u)
        result[u] = min_paths
    return result


def _graph_with_extra_node(graph):
    """
    Al grafo original se añade un nodo adicional 
    que está unido a todos los vértices del grafo con peso 0
    """
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

