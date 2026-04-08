from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n*(n+1)//2
        unique_sum = sum(set(nums))
        actual_sum = sum(nums)
        duplicate = actual_sum - unique_sum
        missing = expected_sum - unique_sum
        return [duplicate, missing]