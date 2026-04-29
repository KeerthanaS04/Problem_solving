from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        # find the median element
        median = nums[len(nums)>>1]
        total_moves = sum(abs(num-median) for num in nums)
        return total_moves