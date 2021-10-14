class Graph:
    def __init__(self):
        self._nodes = set()
        self._graph = {}

    def add_edge(self, u, v, w):
        self._nodes = self._nodes | {u}
        self._nodes = self._nodes | {v}
        value = self._graph.get(u, {})
        value[v] = w
        self._graph[u] = value

    def get_nodes(self):
        return self._nodes

    def get_edges(self):
        return [(entry[0], edge[0], edge[1]) for entry in self._graph.items() for edge in entry[1].items()]

    def get_weight(self, u, v):
        return self._graph[u][v]

    def get_all_adjacent(self, u):
        return self._graph[u].keys()
