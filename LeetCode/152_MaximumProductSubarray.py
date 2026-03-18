from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prodcut = maximum_ending = minimum_ending = nums[0]

        for num in nums[1:]:
            prev_max = maximum_ending
            prev_min = minimum_ending

            maximum_ending = max(num, prev_max*num, prev_min*num)
            minimum_ending = min(num, prev_max*num, prev_min*num)

            max_prodcut = max(max_prodcut, maximum_ending)
        return max_prodcut