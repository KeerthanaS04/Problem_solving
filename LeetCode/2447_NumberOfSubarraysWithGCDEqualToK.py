from typing import List
from math import gcd
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0

        for start_idx in range(len(nums)):
            curr_gcd = 0

            for num in nums[start_idx:]:
                curr_gcd = gcd(curr_gcd, num)
                if curr_gcd == k:
                    count += 1
        return count