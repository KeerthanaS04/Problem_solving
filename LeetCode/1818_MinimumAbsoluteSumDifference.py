from typing import List
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9+7
        sorted_nums1 = sorted(nums1)
        n = len(sorted_nums1)

        # calculate total absolute diff sum
        total_diff = sum(abs(num1-num2) for num1, num2 in zip(nums1, nums2))%MOD

        def find_first_ge(target: int) -> int:
            l, r = 0, n-1
            first_true_idx = -1

            while l<=r:
                mid = (l+r)//2
                if sorted_nums1[mid]>=target:
                    r = mid-1
                    first_true_idx = mid
                else:
                    l = mid+1
            return first_true_idx
        
        max_reduction = 0
        for num1, num2 in zip(nums1, nums2):
            curr_diff = abs(num1-num2)
            min_possible_diff = float('inf')

            idx = find_first_ge(num1)

            if idx!=-1:
                min_possible_diff = min(min_possible_diff, abs(sorted_nums1[idx]-num2))
            
            # check the value before num2
            if idx==-1:
                min_possible_diff = min(min_possible_diff, abs(sorted_nums1[n-1]-num2))
            elif idx>0:
                min_possible_diff = min(min_possible_diff, abs(sorted_nums1[idx-1]-num2))
            reduction = curr_diff-min_possible_diff
            max_reduction = max(max_reduction, reduction)
        return (total_diff-max_reduction+MOD)%MOD