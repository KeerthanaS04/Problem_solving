from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # adjacency matrix with Manhattan distances between all pairs
        graph = [[0]*n for _ in range(n)]
        for i, (x1, y1) in enumerate(points):
            for j in range(i+1, n):
                x2, y2 = points[j]
                manhattan_dist = abs(x1-x2)+abs(y1-y2)
                graph[i][j] = graph[j][i] = manhattan_dist
        
        # arrays for Prim's algorithm
        min_dist = [float('inf')]*n
        visited = [False]*n
        min_dist[0] = 0
        total_cost = 0

        for _ in range(n):
            curr_node = -1
            for node in range(n):
                if not visited[node] and (curr_node==-1 or min_dist[node]<min_dist[curr_node]):
                    curr_node = node
            visited[curr_node] = True
            total_cost+=min_dist[curr_node]

            # for minimum distances for remaining unvisited nodes
            for neighbor in range(n):
                if not visited[neighbor]:
                    min_dist[neighbor] = min(min_dist[neighbor], graph[curr_node][neighbor])
        return total_cost