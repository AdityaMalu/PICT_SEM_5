import networkx as nx
import sys

INF = sys.maxsize

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[INF for _ in range(vertices)] for _ in range(vertices)]
        for i in range(vertices):
            self.adj[i][i] = 0

    def add_edge(self, u, v, weight):
        self.adj[u][v] = weight
        self.adj[v][u] = weight

    def dijkstra(self, src):
        distance = [INF] * self.V
        visited = [False] * self.V

        distance[src] = 0

        for _ in range(self.V - 1):
            u = self.min_distance(distance, visited)
            visited[u] = True

            for v in range(self.V):
                if not visited[v] and self.adj[u][v] != INF and distance[u] != INF and (
                        distance[u] + self.adj[u][v] < distance[v]):
                    distance[v] = distance[u] + self.adj[u][v]

        self.print_shortest_paths(distance, src)

    def min_distance(self, distance, visited):
        min_dist = INF
        min_index = 0
        for v in range(self.V):
            if not visited[v] and distance[v] <= min_dist:
                min_dist = distance[v]
                min_index = v
        return min_index

    def print_shortest_paths(self, distance, src):
        print(f"Shortest Paths from Source {src} to Other Router:")
        for i in range(self.V):
            if i != src:
                print(f"Router {src} to Router {i}: Distance = ", end="")
                if distance[i] == INF:
                    print("No path")
                else:
                    print(distance[i])

def main():
    V = int(input("Enter Number of router: "))
    network = Graph(V)
    source = 0

    while True:
        print("Menu:")
        print("1. Add Edge")
        print("2. Find Shortest Path")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            u = int(input("Enter source router: "))
            v = int(input("Enter destination router: "))
            weight = int(input("Enter link weight: "))
            network.add_edge(u, v, weight)
            print(f"Edge added between router {u} and {v} with weight {weight}.")

        elif choice == 2:
            source = int(input("Enter the source router for the shortest path: "))
            network.dijkstra(source)

        elif choice == 3:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
