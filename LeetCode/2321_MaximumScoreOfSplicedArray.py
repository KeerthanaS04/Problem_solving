from typing import List
class Solution:
    def maximumSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def max_subarray_sum(arr1: List[int], arr2: List[int]) -> int:
            # using kadane's algorithm
            diff = [a-b for a,b in zip(arr1, arr2)]
            curr_sum = max_sum = diff[0]

            for val in diff[1:]:
                if curr_sum>0:
                    curr_sum+=val
                else:
                    curr_sum=val
                max_sum = max(max_sum, curr_sum)
            return max_sum
        sum1, sum2 = sum(nums1), sum(nums2)

        # two scenarios:
        # s2+sum of (nums1[i]-nums2[i]) for i in range(len(nums1))
        # s1+sum of (nums2[i]-nums1[i]) for i in range(len(nums2))
        return max(sum1+max_subarray_sum(nums2, nums1), sum2+max_subarray_sum(nums1, nums2))