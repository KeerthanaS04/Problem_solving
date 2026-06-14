from typing import List
from math import hypot
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point: hypot(point[0], point[1]))
        return points[:k]