from typing import List
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dist = 0
        n2 = len(nums2)

        for i, val in enumerate(nums1):
            left, right = i, n2-1
            first_true_idx = -1

            while left<=right:
                mid = (left+right)//2
                if nums2[mid]<=val:
                    first_true_idx = mid
                    right = mid-1
                else:
                    left = mid+1
            
            # calculate the last valid j
            if first_true_idx==-1:
                # all positions from i to end are valid
                last_valid_j = n2-1
            else:
                last_valid_j = first_true_idx-1
            
            if last_valid_j>=i:
                max_dist = max(max_dist, last_valid_j-i)
        return max_dist