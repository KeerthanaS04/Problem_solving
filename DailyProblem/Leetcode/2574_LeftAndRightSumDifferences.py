from typing import List
class Solution:
    def leftRightDifferences(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        res = []

        for num in nums:
            right_sum -= num
            res.append(abs(left_sum-right_sum))
            left_sum += num
        return res