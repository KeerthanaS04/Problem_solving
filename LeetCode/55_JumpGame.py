from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for curr_pos, jump in enumerate(nums):
            if max_reach<curr_pos:
                return False
            max_reach = max(max_reach, curr_pos+jump)
        return True