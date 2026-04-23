from typing import List
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        visited = {startGene}

        while queue:
            curr_gene, curr_depth = queue.popleft()

            if curr_gene == endGene:
                return curr_depth
            
            for next_gene in bank:
                diff_count = sum(
                    char1!=char2
                    for char1, char2 in zip(curr_gene, next_gene)
                )

                if diff_count==1 and next_gene not in visited:
                    queue.append((next_gene, curr_depth+1))
                    visited.add(next_gene)
        return -1