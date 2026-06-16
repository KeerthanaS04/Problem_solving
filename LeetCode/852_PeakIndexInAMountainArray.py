from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # ignore the first and last element
        l, r = 1, len(arr)-2
        first_true_idx = -1

        while l<=r:
            mid = (l+r)//2
            if arr[mid]>arr[mid+1]:
                first_true_idx = mid
                r = mid-1
            else:
                l = mid+1
        return first_true_idx