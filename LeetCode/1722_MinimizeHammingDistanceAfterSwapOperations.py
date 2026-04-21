from typing import List
from collections import Counter, defaultdict
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSteps: List[List[int]]) -> int:
        def find_root(idx: int) -> int:
            if parent[idx]!=idx:
                parent[idx] = find_root(parent[idx])
            return parent[idx]
        
        # initialize Union-Find Structure
        array_length = len(source)
        parent = list(range(array_length))

        # Union Operation: connect all swappable indices into groups
        for index_a, index_b in allowedSteps:
            parent[find_root(index_a)] = find_root(index_b)
        
        # count frequency of values in each connected component for source array
        component_counts = defaultdict(Counter)
        for i, val in enumerate(source):
            root = find_root(i)
            component_counts[root][val]+=1
        
        # calculates min hamming distance
        hamming_dist = 0
        for i, val in enumerate(target):
            root = find_root(i)
            component_counts[root][val]-=1

            # if count goes negative, this position contribute to hamming distance
            if component_counts[root][val]<0:
                hamming_dist+=1
        return hamming_dist