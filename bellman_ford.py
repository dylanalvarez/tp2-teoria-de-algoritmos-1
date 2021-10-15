import math


def bellman_ford(graph, s):
    """
    Algoritmo de Bellman Ford
    Genera caminos mínimos en el grafo { graph } desde el nodo { s }
    Pre: 
        graph  es un grafo dirigido
        s      es un nodo perteneciente a graph
    Post: 
        distances es un mapa de h(x) donde h(x) es la distancia a x desde s
        en caso de detectar un ciclo de coste total negativo lanza una excepción
    """
    distances = {}
    predecessors = {}
    
    # Para cada nodo en graph
    # se inicializan las distancias en infinito
    # y los predecesores en NULL
    for v in graph.get_nodes():
        distances[v] = math.inf
        predecessors[v] = None

    distances[s] = 0
    edges = graph.get_edges()

    # se relajan |V(graph)| - 1 veces
    for i in range(len(graph.get_nodes()) - 1):
        # cada arista del grafo
        for (u, v, w) in edges:
            if distances[v] > (distances[u] + w):
                distances[v] = distances[u] + w
                predecessors[v] = u

    # Detección de un ciclo de coste total negativo
    for (u, v, w) in edges:
        if distances[v] > (distances[u] + w):
            # Para este grafo no habrá solución para el algoritmo de bellman ford
            raise RuntimeError("Negative cycle")

    return distances
