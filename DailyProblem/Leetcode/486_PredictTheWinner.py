from typing import List
from functools import cache
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(l: int, r: int) -> int:
            # no elements left to pick
            if l>r:
                return 0

            pick_left = nums[l]-dfs(l+1, r)
            pick_right = nums[r]-dfs(l, r-1)
            return max(pick_left, pick_right)
        return dfs(0, len(nums)-1)>=0