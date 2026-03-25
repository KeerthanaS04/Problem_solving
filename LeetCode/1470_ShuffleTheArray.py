from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half = nums[:n]
        second_half = nums[n:]

        result = [element for pair in zip(first_half, second_half) for element in pair]
        return result