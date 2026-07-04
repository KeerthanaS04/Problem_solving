from typing import List
from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node_a, node_b, dist in roads:
            graph[node_a].append((node_b, dist))
            graph[node_b].append((node_a, dist))
        
        visited = [False] * (n + 1)
        min_score = float('inf')

        def dfs(curr_node):
            nonlocal min_score

            for neighbor, weight in graph[curr_node]:
                min_score = min(min_score, weight)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        visited[1] = True
        dfs(1)
        return min_score