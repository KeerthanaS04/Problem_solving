from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        nonzeroIndex = 0

        for i in range(n):
            if nums[i]!=0:
                nums[nonzeroIndex], nums[i] = nums[i], nums[nonzeroIndex]
                nonzeroIndex+=1