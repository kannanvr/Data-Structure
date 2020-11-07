from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs_traversal(self, source):  # time=O(V+E), traverse adjacency list)
        visited = [False] * len(self.graph)
        q = [source]
        visited[source] = True
        while len(q) > 0:
            current_vertex = q.pop(0)
            print(current_vertex, end=' ')
            # traverse to all neighbours of current_vertex and push those neighbours which are not yet visited in a queue
            for neighbour in self.graph[current_vertex]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    visited[neighbour] = True
        print("visited array", visited)

    def bfs_traversal_line_by_line(self, source):
        visited = [False] * len(self.graph)
        q = [source]
        visited[source] = True
        while len(q) > 0:
            l, count = [], len(q)
            while count > 0:
                current_vertex = q.pop(0)
                l.append(current_vertex)
                # traverse to all neighbours of current_vertex and push those neighbours which are not yet visited in
                # a queue
                for neighbour in self.graph[current_vertex]:
                    if not visited[neighbour]:
                        q.append(neighbour)
                        visited[neighbour] = True
                count -= 1
            print(l)
        print("visited array", visited)

    def printGraph(self):
        print(self.graph)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.printGraph()
print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.bfs_traversal(2)
g.bfs_traversal_line_by_line(2)
