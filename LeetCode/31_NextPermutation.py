from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # find the rightmost ascending pair
        pivot_idx = -1
        for i in range(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                pivot_idx = i
                break
        
        # if pivot exists, find the smallest element greater than pivot from the right
        if pivot_idx!=-1:
            swap_idx = -1
            for i in range(n-1, pivot_idx, -1):
                if nums[i]>nums[pivot_idx]:
                    swap_idx = i
                    break
            
            # swap the pivot with the found element
            nums[pivot_idx], nums[swap_idx] = nums[swap_idx], nums[pivot_idx]
        
        # reverses the suffix after pivot_idx to get the next smaller permutation
        left = pivot_idx+1
        right = n-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1