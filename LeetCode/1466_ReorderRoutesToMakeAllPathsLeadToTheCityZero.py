from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def count_reversal(current: int, parent: int) -> int:
            total_reversals = 0
            # visit all neighbors
            for neighbor, need_reversal in adjacency_list[current]:
                if neighbor!=current:
                    total_reversals+=need_reversal+count_reversal(neighbor, current)
            return total_reversals
        
        adjacency_list = [[] for _ in range(n)]
        for from_city, to_city in connections:
            # costs 1 to reverse
            adjacency_list[from_city].append((to_city, 1))
            # already points to the root direction
            adjacency_list[to_city].append((from_city, 0))
        return count_reversal(0, -1)