from typing import List
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        count = sum(
            i!=j and nums[i]+nums[j]==target for i in range(n) for j in range(n)
        )
        return count