from typing import List
class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(
            sum(int(digit) for digit in str(number))
            for number in nums
        )