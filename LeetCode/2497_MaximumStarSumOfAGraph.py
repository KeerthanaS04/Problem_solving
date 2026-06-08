from typing import List
from collections import defaultdict
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)

        for node_a, node_b in edges:
            if vals[node_b]>0:
                graph[node_a].append(vals[node_b])
            if vals[node_a]>0:
                graph[node_b].append(vals[node_a])
        
        # sort each node's neighbor values in descending order
        for neighbor_val in graph.values():
            neighbor_val.sort(reverse=True)

        # calculate maximum star sum
        max_sum = float('inf')
        for node_idx, node_val in enumerate(vals):
            star_sum = node_val+sum(graph[node_idx][:k])
            max_sum = max(max_sum, star_sum)
        return max_sum