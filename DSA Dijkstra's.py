#Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a weighted graph.

class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[0]*size for i in range(size)]
        self.vertex_data = ['']*size
    def add_edge(self, u, v, weight):
        if 0 <= self.size and 0 <= self.size:
            self.adj_matrix[u][v]= weight
            self.adj_matrix[v][u] = weight
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i
            if u is None:
                break

            visited[u] = True
            for j in range(self.size):
                if self.adj_matrix[u][j] != 0 and not visited[j]:
                    alt = distances[u] + self.adj_matrix[u][j]
                    if alt < distances[j]:
                        distances[j] = alt
        return distances
g = Graph(9)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
g.add_vertex_data(7, 'H')
g.add_vertex_data(8, 'I')

g.add_edge(3, 1, 4)
g.add_edge(3, 3, 2)
g.add_edge(4, 1, 5)
g.add_edge(2, 5, 6)
g.add_edge(5, 3, 5)
g.add_edge(1, 7, 7)
g.add_edge(6, 5, 2)
g.add_edge(8, 2, 3)
g.add_edge(0, 5, 7)

print("\nDijkstra's Algorithm starting form vertex D:")
distances = g.dijkstra('D')
for i, d in enumerate(distances):
    print(f"Distance from D to {g.vertex_data[i]}: {d}")



