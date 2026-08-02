import heapq
class Solution:
    def shortestPath(self, V: int, src: int, dest: int, edges: list[list[int]]) -> int:
        # build adjacency list
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # distance array
        dist = [float('inf')]*V
        dist[src] = 0

        # min heap: (dist, node)
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)

            # ignore outdated entries
            if d > dist[u]:
                continue

            # relax all neighbors
            for v, w in adj[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        return -1 if dist[dest] == float('inf') else dist[dest]