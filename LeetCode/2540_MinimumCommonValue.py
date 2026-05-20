from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pointer1 = 0
        pointer2 = 0

        l1 = len(nums1)
        l2 = len(nums2)

        while pointer1<l1 and pointer2<l2:
            if nums1[pointer1]==nums2[pointer2]:
                return nums1[pointer1]
            
            # move the pointer pointing to the small value
            if nums1[pointer1]<nums2[pointer2]:
                pointer1+=1
            else:
                pointer2+=1
        return -1