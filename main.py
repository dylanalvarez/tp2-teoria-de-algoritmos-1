import sys
from graph import Graph
from johnson import johnson


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
    johnson(graph)
    return 0

if __name__ == "__main__":
    if len(sys.argv) > 1:
        exit_code = main(sys.argv[1])
    else:
        print("A filename is required as a parameter")
        exit_code = 1
    sys.exit(exit_code)
