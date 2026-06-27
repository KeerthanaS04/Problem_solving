from typing import List
from itertools import pairwise
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        max_consecutive = max(special[0]-bottom, top-special[-1])

        for curr_floor, next_floor in pairwise(special):
            gap = next_floor-curr_floor-1
            max_consecutive = max(max_consecutive, gap)
        return max_consecutive