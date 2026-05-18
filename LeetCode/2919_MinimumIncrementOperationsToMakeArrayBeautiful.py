from typing import List
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp_prev2 = 0
        dp_prev1 = 0
        dp_curr = 0

        for num in nums:
            # how much to increment curr element
            increment = max(k-num, 0)
            dp_prev2, dp_prev1, dp_curr = dp_prev1, dp_curr, min(dp_prev2, dp_prev1, dp_curr)+increment
        return min(dp_prev2, dp_prev1, dp_curr)