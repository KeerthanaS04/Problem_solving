from functools import cache
from math import inf
from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(curr_idx: int) -> int:
            # base case: reached the last index
            if curr_idx==n-1:
                return 0
            max_jumps = -inf
            for next_idx in range(curr_idx+1, n):
                if abs(nums[curr_idx]-nums[next_idx]) <= target:
                    max_jumps = max(max_jumps, 1 + dfs(next_idx))
            return max_jumps
        n = len(nums)
        res = dfs(0)
        return -1 if res<0 else res