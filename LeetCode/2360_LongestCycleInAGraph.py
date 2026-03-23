from typing import List
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False]*n
        max_cycle_length = -1

        for start_node in range(n):
            if visited[start_node]:
                continue
            curr_node = start_node
            path = []
            while curr_node!=-1 and not visited[curr_node]:
                visited[curr_node] = True
                path.append(curr_node)
                curr_node = edges[curr_node]
            # if we hit a dead end, skip
            if curr_node==-1:
                continue

            path_length = len(path)
            cycle_start_idx = float('inf')
            for index in range(path_length):
                if path[index]==curr_node:
                    cycle_start_idx = index
                    break
            cycle_length = path_length-cycle_start_idx
            max_cycle_length = max(max_cycle_length, cycle_length)
        return max_cycle_length
