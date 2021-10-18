from graph import Graph
from bellman_ford import bellman_ford


# Se prueba con el grafo del informe


def test_bellman_ford():
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

    def test_bellman_ford_from_A(graph):
        response = bellman_ford(graph, "A")
        assert response["A"] == 0
        assert response["B"] == 0
        assert response["C"] == -5
        assert response["D"] == -2
        assert response["E"] == 2

    def test_bellman_ford_from_B(graph):
        response = bellman_ford(graph, "B")
        assert response["A"] == 0
        assert response["B"] == 0
        assert response["C"] == -5
        assert response["D"] == -2
        assert response["E"] == 2

    def test_bellman_ford_from_C(graph):
        response = bellman_ford(graph, "C")
        assert response["A"] == 6
        assert response["B"] == 6
        assert response["C"] == 0
        assert response["D"] == 3
        assert response["E"] == 8

    def test_bellman_ford_from_D(graph):
        response = bellman_ford(graph, "D")
        assert response["A"] == 4
        assert response["B"] == 4
        assert response["C"] == -2
        assert response["D"] == 0
        assert response["E"] == 5

    def test_bellman_ford_from_E(graph):
        response = bellman_ford(graph, "E")
        assert response["A"] == -1
        assert response["B"] == -1
        assert response["C"] == -7
        assert response["D"] == -4
        assert response["E"] == 0

    test_bellman_ford_from_A(graph)
    test_bellman_ford_from_B(graph)
    test_bellman_ford_from_C(graph)
    test_bellman_ford_from_D(graph)
    test_bellman_ford_from_E(graph)
