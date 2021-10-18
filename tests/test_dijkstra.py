from graph import Graph
from dijkstra import dijkstra


# Se prueba con el grafo del informe


def test_dijkstra():
    graph = Graph()
    graph.add_edge("A", "B", 0)
    graph.add_edge("B", "A", 0)
    graph.add_edge("C", "A", 0)
    graph.add_edge("C", "D", 0)
    graph.add_edge("D", "A", 1)
    graph.add_edge("A", "E", 1)
    graph.add_edge("E", "C", 0)
    graph.add_edge("D", "E", 1)
    graph.add_edge("E", "D", 1)

    def test_dijkstra_from_A(graph):
        response = dijkstra(graph, "A")
        assert response["A"] == 0
        assert response["B"] == 0
        assert response["C"] == 1
        assert response["D"] == 1
        assert response["E"] == 1

    def test_dijkstra_from_B(graph):
        response = dijkstra(graph, "B")
        assert response["A"] == 0
        assert response["B"] == 0
        assert response["C"] == 1
        assert response["D"] == 1
        assert response["E"] == 1

    def test_dijkstra_from_C(graph):
        response = dijkstra(graph, "C")
        assert response["A"] == 0
        assert response["B"] == 0
        assert response["C"] == 0
        assert response["D"] == 0
        assert response["E"] == 1

    def test_dijkstra_from_D(graph):
        response = dijkstra(graph, "D")
        assert response["A"] == 1
        assert response["B"] == 1
        assert response["C"] == 1
        assert response["D"] == 0
        assert response["E"] == 1

    def test_dijkstra_from_E(graph):
        response = dijkstra(graph, "E")
        assert response["A"] == 0
        assert response["B"] == 0
        assert response["C"] == 0
        assert response["D"] == 0
        assert response["E"] == 0

    test_dijkstra_from_A(graph)
    test_dijkstra_from_B(graph)
    test_dijkstra_from_C(graph)
    test_dijkstra_from_D(graph)
    test_dijkstra_from_E(graph)