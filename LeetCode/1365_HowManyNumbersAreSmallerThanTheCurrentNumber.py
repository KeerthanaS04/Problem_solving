from typing import List
from bisect import bisect_left
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        result = [bisect_left(sorted_nums, num) for num in nums]
        return result