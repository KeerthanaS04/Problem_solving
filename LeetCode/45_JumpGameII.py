from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_cnt = 0
        maxi = 0 # farthest we can reach
        last = 0 # curr jump boundary

        # we don't need to check the last element since we want to reach it, not jump from it
        for i in range(len(nums)-1):
            maxi = max(maxi, i+nums[i])
            if i==last:
                jump_cnt += 1
                last = maxi
        return jump_cnt