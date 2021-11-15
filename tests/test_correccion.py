from graph import Graph
from johnson import johnson
from main import print_result

# Se prueba con el grafo de las correcciones
def test_johnson():
    graph = Graph()
    graph.add_edge("A", "B", 3)
    graph.add_edge("A", "C", 8)
    graph.add_edge("A", "E", -4)
    graph.add_edge("B", "E", 7)
    graph.add_edge("B", "D", 1)
    graph.add_edge("C", "B", 4)
    graph.add_edge("D", "C", -5)
    graph.add_edge("D", "A", 2)
    graph.add_edge("E", "D", 6)
    response, min_node = johnson(graph)
    assert min_node == "D"
