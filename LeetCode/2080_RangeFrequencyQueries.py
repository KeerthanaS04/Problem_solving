from collections import defaultdict
from bisect import bisect_left, bisect_right
from typing import List
class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.val_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            self.val_to_indices[val].append(i)
    
    def query(self, left: int, right: int, value: int) -> int:
        indices = self.val_to_indices[value]
        left_pos = bisect_left(indices, left)
        right_pos = bisect_right(indices, right)
        return right_pos - left_pos