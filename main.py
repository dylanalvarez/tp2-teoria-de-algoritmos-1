import sys
from johnson import johnson

def main(path):
  try:
    graph_file = open(path, 'r')
    graph = {}

    for edge in graph_file.read().splitlines():
      (from_n, to_n, edge_value) = edge.upper().split(',')
      value = graph.get(from_n, {})
      value[to_n] = int(edge_value)
      graph[from_n] = value

    johnson(graph)
    return 0
  except:
    print("The content of the file is wrong")
    return 1

if __name__ == "__main__":
  if len(sys.argv) > 1:
    exit_code = main(sys.argv[1])
  else:
    print("A filename is required as a parameter")
    exit_code = 1
  sys.exit(exit_code)
