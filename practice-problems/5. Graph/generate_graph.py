'''
defaultdict: Usually, a Python dictionary throws a KeyError if you try to get an item with a key that is not currently
in the dictionary. defaultdict allows that if a key is not found in the dictionary, then instead of a KeyError being thrown,
a new entry is created. The type of this new entry is given by the argument of defaultdict.
'''
# import dictionary for graph
from collections import defaultdict

# function for adding edge to graph
graph = defaultdict(list)


def addEdge(graph, u, v):
    graph[u].append(v)


# definition of function
def generate_edges(graph):
    edges = []
    # for each node in graph
    for node in graph:
        # for each neighbour node of a single node
        for neighbour in graph[node]:
            # if edge exists then append
            edges.append((node, neighbour))
    return edges


# declaration of graph as dictionary
addEdge(graph, 'a', 'c')
addEdge(graph, 'b', 'c')
addEdge(graph, 'b', 'e')
addEdge(graph, 'c', 'd')
addEdge(graph, 'c', 'e')
addEdge(graph, 'c', 'a')
addEdge(graph, 'c', 'b')
addEdge(graph, 'e', 'b')
addEdge(graph, 'd', 'c')
addEdge(graph, 'e', 'c')
print("Adjacency List Representation Of Above Graph\n", graph)
# Driver Function call
# to print generated graph
print(generate_edges(graph))
