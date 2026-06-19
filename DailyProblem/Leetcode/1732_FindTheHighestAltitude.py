from typing import List
from itertools import accumulate
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        heights = accumulate(gain, initial=0)
        return max(heights)