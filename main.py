import sys
from graph import Graph
from johnson import johnson


def print_result(min_paths_by_node):
    min_node = list(min_paths_by_node.keys())[0]
    min_value = sum(min_paths_by_node[min_node].values())
    for (u, min_paths) in min_paths_by_node.items():
        value = sum(min_paths.values())
        if value < min_value:
            min_node = u
            min_value = value
    print("El depósito debe ir en la ciudad:", min_node)
    print("Costos mínimos entre depósitos:")
    print("{:^4}".format(" "), end=" ")
    sorted_keys = sorted(min_paths_by_node.keys())
    for u in sorted_keys:
        print("{:^4}".format(u), end=" ")
    print("")

    for u in sorted_keys:
        print("{:^4}".format(u), end=" ")
        for v in sorted_keys:
            print("{:^4}".format(min_paths_by_node[v][u]), end=" ")
        print("")


def main(path):
    try:
        graph_file = open(path, 'r')
        edges = []

        for edge in graph_file.read().splitlines():
            (u, v, w) = edge.split(',')
            edges.append((u, v, int(w)))
    except:
        print("The content of the file is wrong")
        return 1

    graph = Graph()

    for (u, v, w) in edges:
        graph.add_edge(u, v, w)

    print_result(johnson(graph))
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        exit_code = main(sys.argv[1])
    else:
        print("A filename is required as a parameter")
        exit_code = 1
    sys.exit(exit_code)
