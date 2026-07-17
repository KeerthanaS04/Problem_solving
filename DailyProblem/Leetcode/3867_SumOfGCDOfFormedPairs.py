from typing import List
from math import gcd
class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*n
        mx = 0
        for i, x in enumerate(nums):
            mx = max(mx, x)
            prefix[i] = gcd(mx, x)
        prefix.sort()
        return sum(gcd(prefix[i], prefix[-i-1]) for i in range(n//2))