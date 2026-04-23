from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Cyclic sort
        for i in range(len(nums)):
            while nums[i]!=nums[nums[i]-1]:
                correct_idx = nums[i]-1
                nums[correct_idx], nums[i] = nums[i], nums[correct_idx]
        duplicates = []
        for i, val in enumerate(nums):
            if val!=i+1:
                duplicates.append(val)
        return  duplicates