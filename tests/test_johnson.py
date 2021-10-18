from graph import Graph
from johnson import johnson
from main import print_result

# Se prueba con el grafo del informe


def test_johnson():
    graph = Graph()
    graph.add_edge("A", "B", 0)
    graph.add_edge("B", "A", 0)
    graph.add_edge("C", "A", 6)
    graph.add_edge("C", "D", 3)
    graph.add_edge("D", "A", 4)
    graph.add_edge("A", "E", 2)
    graph.add_edge("E", "C", -7)
    graph.add_edge("D", "E", 5)
    graph.add_edge("E", "D", -3)
    response, min_node = johnson(graph)
    assert min_node == "E"
