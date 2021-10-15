import math
from heapq import heappush, heappop


def dijkstra(graph, s):
    """
    Implementación del algoritmo de Dijkstra utilizando cola de prioridad
    Genera caminos mínimos en el grafo { graph } desde el nodo { s }
    Pre:
        graph  es un grafo dirigido con pesos no negativos
        s      es un nodo perteneciente a graph
    Post:
        distances es un mapa de h(x) donde h(x) es la distancia a x desde s
    """
    h = []
    distances = {}
    parents = {}
    seen = {}

    # Para cada nodo en graph
    # se inicializan las distancias en infinito
    # y los predecesores en NULL
    for u in graph.get_nodes():
        distances[u] = math.inf
        parents[u] = None
        seen[u] = False
    distances[s] = 0
    heappush(h, (distances[s], s))

    while len(h):
        # se obtiene el mínimo de la cola de prioridad
        # correspondiente a la distancia más pequeña a un nodo
        u = heappop(h)[1]
        seen[u] = True
        # para todos los nodos adyacentes a u no vistos
        # 
        for v in graph.get_all_adjacent(u):
            if seen[v]:
                continue
            # en caso de que la distancia tentativa desde v a u 
            # sea menor a la almacenada
            # se actualiza
            if distances[v] > (distances[u] + graph.get_weight(u, v)):
                distances[v] = distances[u] + graph.get_weight(u, v)
                parents[v] = u
                heappush(h, (distances[v], v))
    return distances
