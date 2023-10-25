class LinkStateRoutingProtocol:
    def __init__(self):
        self.nodes = []
        self.routing_table = {}

    def add_node(self, node):
        self.nodes.append(node)

    def build_routing_table(self):
        for node in self.nodes:
            self.routing_table[node.name] = self.get_shortest_path(node)

    def get_shortest_path(self, source_node):
        distance_vector = {node.name: float('inf') for node in self.nodes}
        distance_vector[source_node.name] = 0
        unvisited = set(node.name for node in self.nodes)

        while unvisited:
            current_node = min(unvisited, key=lambda n: distance_vector[n])
            unvisited.remove(current_node)

            for neighbor_name, cost in source_node.costs.items():
                if neighbor_name in unvisited:
                    new_distance = distance_vector[current_node] + cost
                    if new_distance < distance_vector[neighbor_name]:
                        distance_vector[neighbor_name] = new_distance

        return distance_vector

    def get_route(self, source, destination):
        if source not in self.routing_table or destination not in self.routing_table:
            return None

        path = [destination]  # Start building the path from the destination node
        while source != destination:
            next_hop = min(
                self.routing_table[source],
                key=lambda n: self.routing_table[source][n]
            )
            path.append(next_hop)
            destination = next_hop

        return path[::-1]  # Reverse the path to get it from source to destination

class Node:
    def __init__(self, name, neighbors, costs):
        self.name = name
        self.neighbors = neighbors
        self.costs = {n: c for n, c in zip(neighbors, costs)}

if __name__ == "__main__":
    routing_protocol = LinkStateRoutingProtocol()

    nodes = [
        Node("A", ["B", "C"], [1, 2]),
        Node("B", ["A", "C", "D"], [1, 2, 3]),
        Node("C", ["A", "B", "D", "E"], [2, 2, 3, 4]),
        Node("D", ["B", "C", "E"], [3, 3, 4]),
        Node("E", ["C", "D"], [4, 4])
    ]

    for node in nodes:
        routing_protocol.add_node(node)

    routing_protocol.build_routing_table()

    print("Routing table:")
    for node, routing_table in routing_protocol.routing_table.items():
        print(f"{node}: {routing_table}")

    print("Get route from A to E:")
    route = routing_protocol.get_route("A", "E")
    print(f"Route: {route}")
    print("Get route from B to F:")
    route = routing_protocol.get_route("B", "D")
    print(f"Route: {route}")