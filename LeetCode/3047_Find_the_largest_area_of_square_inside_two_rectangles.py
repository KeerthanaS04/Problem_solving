from typing import List
from itertools import combinations
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_sq_area = 0
        for ((x1,y1), (x2,y2)), ((x3,y3), (x4,y4)) in combinations(zip(bottomLeft, topRight), 2):
            w = min(x2, x4) - max(x1, x3)
            h = min(y2, y4) - max(y1, y3)
            max_side = min(h, w)

            if max_side>0:
                sq_area = max_side**2
                max_sq_area = max(max_sq_area, sq_area)
        return max_sq_area