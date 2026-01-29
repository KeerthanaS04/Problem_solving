from typing import List
from math import inf
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # graph[i][j] represents the minimumcost to transform character i to j
        graph = [[inf]*26 for _ in range(26)]

        # Cost of transforming to itself is 0
        for i in range(26):
            graph[i][i] = 0
        
        # Build the graph with the given transformations
        for x, y, z in zip(original, changed, cost):
            from_index = ord(x)-ord('a')
            to_index = ord(y)-ord('a')
            graph[from_index][to_index] = min(graph[from_index][to_index], z)
        
        # Floyd-Warshall Algorithm to find shortest paths bewtween all pairs
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
        
        # Calculate minimum total cost to transform
        total = 0
        for a, b in zip(source, target):
            if a!=b:
                from_index = ord(a)-ord('a')
                to_index = ord(b)-ord('a')

                #check if transformation is possible
                if graph[from_index][to_index]>=inf:
                    return -1
                total+=graph[from_index][to_index]
        return total