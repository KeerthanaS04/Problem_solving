from collections import defaultdict
from math import inf
from typing import List
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        g = defaultdict(list)
        for i, x in enumerate(nums):
            g[x].append(i)
        ans = inf
        for ls in g.values():
            for h in range(len(ls)-2):
                i, k = ls[h], ls[h+2]
                # j-i+k-j+k-i = 2*(k-i)
                ans = min(ans, 2*(k-i))
        return -1 if ans==inf else ans