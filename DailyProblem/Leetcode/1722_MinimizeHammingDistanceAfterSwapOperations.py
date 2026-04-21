from collections import Counter
from collections import defaultdict
from typing import List
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        def find_root(idx: int) -> int:
            if parent[idx]!=idx:
                parent[idx] = find_root(parent[idx])
            return parent[idx]
        
        # initialize Union-Find structure
        array_length = len(source)
        parent = list(range(array_length))

        # Union operation: connect all swappable indices into groups
        for index_a, index_b in allowedSwaps:
            parent[find_root(index_a)] = find_root(index_b)

        # count frequency of values in each connected component for source array
        component_counts = defaultdict(Counter)
        for i, val in enumerate(source):
            root = find_root(i)
            component_counts[root][val]+=1
        
        # calculate the hamming distance
        hamming_dist = 0
        for i, val in enumerate(target):
            root = find_root(i)
            component_counts[root][val]-=1
            
            # if count goes negative, this position contributes to hamming distance
            if component_counts[root][val]<0:
                hamming_dist+=1
        return hamming_dist