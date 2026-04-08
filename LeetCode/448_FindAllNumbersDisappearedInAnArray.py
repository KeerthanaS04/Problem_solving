from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers_present = set(nums)
        missing = [
            number 
            for number in range(1, len(nums)+1)
            if number not in numbers_present
        ]
        return missing