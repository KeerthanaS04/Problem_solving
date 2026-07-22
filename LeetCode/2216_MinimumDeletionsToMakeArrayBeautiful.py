from typing import List
class Solution:
    def minDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        idx = 0
        deletions = 0

        while idx<n-1:
            if nums[idx]==nums[idx+1]:
                deletions+=1
                idx+=1
            else:
                idx+=2

        deletions+=(n-deletions)//2
        return deletions