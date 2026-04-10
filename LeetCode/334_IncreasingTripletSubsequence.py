from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<3:
            return False
        
        small = [0]*n
        big = [0]*n

        # fill small
        small[0] = nums[0]
        for i in range(1, n):
            small[i] = min(nums[i], small[i-1])
        
        # fill big
        big[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            big[i] = max(nums[i], big[i+1])
        
        # find valid triplet
        for i in range(n):
            if nums[i]>small[i] and nums[i]<big[i]:
                return True
        return False