from typing import List
from math import gcd
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def lcm(a: int, b: int) -> int:
            return abs(a*b)//gcd(a, b)
        
        n = len(nums)
        count = 0

        for start_idx in range(n):
            curr_lcm = nums[start_idx]

            for num in nums[start_idx:]:
                curr_lcm = lcm(curr_lcm, num)
                if curr_lcm == k:
                    count += 1
                if curr_lcm > k:
                    break
        return count