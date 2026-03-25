from typing import List
from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adjacency_list = [[] for _ in range(n)]
        node_degrees = [0]*n

        for node_a, node_b in edges:
            adjacency_list[node_a].append(node_b)
            adjacency_list[node_b].append(node_a)
            node_degrees[node_a]+=1
            node_degrees[node_b]+=1
        
        # initialize queue with all leaf nodes (degree=1)
        leaves_queue = deque(node for node in range(n) if node_degrees[node]==1)
        remaining_nodes = []

        while leaves_queue:
            remaining_nodes.clear()
            curr_size = len(leaves_queue)
            for _ in range(curr_size):
                leaf_node = leaves_queue.popleft()
                remaining_nodes.append(leaf_node)

                for neighbor in adjacency_list[leaf_node]:
                    node_degrees[neighbor]-=1
                    if node_degrees[neighbor]==1:
                        leaves_queue.append(neighbor)
        return remaining_nodes