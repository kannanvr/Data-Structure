from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs_traversal(self, source, visited):
        visited[source] = True
        print(source, end=' ')
        for neighbour in self.graph[source]:
            if not visited[neighbour]:
                self.dfs_traversal(neighbour, visited)

        # prints all not yet visited vertices reachable from s
    def dfs_traversal_using_stack(self, s):  # prints all vertices in DFS manner from a given source.
        # Initially mark all verices as not visited
        visited = [False]*len(self.graph)
        # Create a stack for DFS
        stack = [s]
        # Push the current source node.
        while len(stack):
            # Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()
            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if not visited[s]:
                print(s, end=' ')
                visited[s] = True
            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for node in self.graph[s]:
                if not visited[node]:
                    stack.append(node)

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
print("Following is depth First Traversal"
      " (starting from vertex 2)")
visited = [False] * len(g.graph)
for i in range(0,len(g.graph)):
    print("dfs starting from ",i)
    g.dfs_traversal(i, visited)
    print()
print("dfs using stack -----")
g.dfs_traversal_using_stack(0)
