from typing import List
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        s1 = s2 = 0
        i = j = 0
        ans = 0

        while i < m and j < n:
            if nums1[i]==nums2[j]:
                ans += max(s1, s2) + nums1[i]
                s1 = s2 = 0
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                s1 += nums1[i]
                i += 1
            else:
                s2 += nums2[j]
                j += 1
        
        while i < m:
            s1 += nums1[i]
            i += 1
        
        while j < n:
            s2 += nums2[j]
            j += 1
        
        ans+= max(s1, s2)
        return ans % (10**9 + 7)