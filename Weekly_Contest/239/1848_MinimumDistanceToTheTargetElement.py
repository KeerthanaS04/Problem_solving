from typing import List
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min(abs(i-start) for i, value in enumerate(nums) if value==target)