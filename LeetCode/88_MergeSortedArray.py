from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merge_idx = n+m-1
        nums1_idx = m-1
        nums2_idx = n-1

        while nums2_idx>=0:
            if nums1_idx>=0 and nums1[nums1_idx]>nums2[nums2_idx]:
                nums1[merge_idx] = nums1[nums1_idx]
                nums1_idx-=1
            else:
                nums1[merge_idx] = nums2[nums2_idx]
                nums2_idx-=1
            merge_idx-=1