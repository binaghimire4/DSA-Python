#A graph is a non-linear data structure in dsa that consists of a set of vertices and a set of edges connect pairs of vertices.

class graph:
    def __init__(self, size):
        self.adj_matrix = [[0]* size for i in range(size)]
        self.size = size
        self.vertex_data = ['']* size

    def add_edge(self, u,v):
        if 0 <=u < self.size and 0 <= v < self.size:
            self.adj_matrix [u][v] = 1
            self.adj_matrix[u][v] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex]= data

    def print_graph(self):
        print("Adjancency matraix:")
        for row in self.adj_matrix:
            print(''.join(map(str,row)))
        print("\nVertex data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"vertex{vertex}:{data}")
g = graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,1)

g.print_graph()

from collections import deque


def bfs(graph, start, search_value):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex == search_value:
            return True
        visited.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return False


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = "F"
search_value = "B"
res = bfs(graph, start, search_value)
print(f"element {search_value} : {res}")

