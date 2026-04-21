from typing import List
from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find_root(node: int) -> int:
            if parent[node]!=node:
                parent[node] = find_root(parent[node])
            return parent[node]
        n = len(s)
        parent = list(range(n))

        # Union operation: connect all indices that can be swapped
        for index_a, index_b in pairs:
            parent[find_root(index_a)] = find_root(index_b)
        
        component_chars = defaultdict(list)
        for i, char in enumerate(s):
            root = find_root(i)
            component_chars[root].append(char)
        
        # sort characters in descending order
        for root in component_chars.keys():
            component_chars[root].sort(reverse=True)
        
        res = []
        for i in range(n):
            root = find_root(i)
            res.append(component_chars[root].pop())
        return ''.join(res)