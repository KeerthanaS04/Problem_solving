from bisect import bisect_right
from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_sorted = sorted(set(arr))

        return [bisect_right(unique_sorted, x) for x in arr]