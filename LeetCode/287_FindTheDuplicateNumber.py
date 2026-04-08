from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        left, right = 1, n
        true_index = -1

        while left<=right:
            mid = (left+right)//2
            count = sum(1 for num in nums if num<=mid)

            if count>mid:
                true_index = mid
                right = mid-1
            else:
                left = mid+1
        return true_index