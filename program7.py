from typing import List
import heapq


class ShortestPath:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append((u, v, weight))

    # -------------------------
    # Dijkstra's Algorithm
    # -------------------------
    def dijkstra(self, src: int) -> List[int]:
        graph = [[] for _ in range(self.vertices)]

        for u, v, weight in self.edges:
            graph[u].append((v, weight))

        distance = [float('inf')] * self.vertices
        distance[src] = 0

        pq = [(0, src)]

        while pq:
            dist, u = heapq.heappop(pq)

            if dist > distance[u]:
                continue

            for v, weight in graph[u]:
                new_dist = dist + weight

                if new_dist < distance[v]:
                    distance[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return distance

    # -------------------------
    # Bellman-Ford Algorithm
    # -------------------------
    def bellman_ford(self, src: int) -> List[int]:
        distance = [float('inf')] * self.vertices
        distance[src] = 0

        # Relax all edges V-1 times
        for _ in range(self.vertices - 1):
            changed = False

            for u, v, weight in self.edges:
                if distance[u] != float('inf') and \
                   distance[u] + weight < distance[v]:

                    distance[v] = distance[u] + weight
                    changed = True

            if not changed:
                break

        # Check for negative cycle
        for u, v, weight in self.edges:
            if distance[u] != float('inf') and \
               distance[u] + weight < distance[v]:
                return ["Negative cycle"]

        return distance


# -------------------------
# Example
# -------------------------

g = ShortestPath(5)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)
g.add_edge(3, 4, 3)

print("Dijkstra:", g.dijkstra(0))
print("Bellman-Ford:", g.bellman_ford(0))
