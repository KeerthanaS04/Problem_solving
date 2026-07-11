from typing import List
from collections import defaultdict
import heapq
from math import inf
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> int:
        graph = defaultdict(list)
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        
        dist = [inf]*n
        dist[0] = 0 # starting node has distance 0
        priority_queue = [(0, 0)] # priority queue for dijkstra's algorithm

        # dijkstra's algorithm
        while priority_queue:
            curr_dist, curr_node = heapq.heappop(priority_queue)

            if curr_dist > dist[curr_node]:
                continue

            # explore all adjacent nodes
            for neigh, weight in graph[curr_node]:
                new_dist = dist[curr_node] + weight

                if dist[neigh] > new_dist and new_dist < disappear[neigh]:
                    dist[neigh] = new_dist
                    heapq.heappush(priority_queue, (new_dist, neigh))
        
        res = []
        for distance, disappear_time in zip(dist, disappear):
            if distance < disappear_time:
                res.append(distance)
            else:
                res.append(-1)
        return res