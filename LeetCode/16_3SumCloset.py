from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n):
            l = i+1
            r = n-1
            while l<r:
                curr_sum = nums[i]+nums[l]+nums[r]
                if curr_sum == target:
                    return target
                if abs(curr_sum-target)<abs(closest_sum-target):
                    closest_sum = curr_sum
                if curr_sum > target:
                    r -= 1
                else:
                    l += 1
        return closest_sum