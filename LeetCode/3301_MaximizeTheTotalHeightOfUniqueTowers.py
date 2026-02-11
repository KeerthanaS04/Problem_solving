from math import inf
from typing import List
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort()

        maxi = inf
        total = 0

        for max_height in maximumHeight[::-1]:
            h = min(max_height, maxi-1)

            if h<=0:
                return -1
            total+=h
            maxi = h

        return total