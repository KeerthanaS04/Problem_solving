from collections import Counter
from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree_count = Counter(destination for source, destination in edges)
        res = [vertex for vertex in range(n) if in_degree_count[vertex]==0]
        return res