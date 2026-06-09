from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = float('-inf')
        min_prefix_before = {nums[0]:0}
        prefix_sum = 0
        n = len(nums)

        for i, curr_num in enumerate(nums):
            prefix_sum+=curr_num

            if curr_num-k in min_prefix_before:
                max_sum = max(max_sum, prefix_sum-min_prefix_before[curr_num-k])
            
            if curr_num+k in min_prefix_before:
                max_sum = max(max_sum, prefix_sum-min_prefix_before[curr_num+k])
            
            # update min prefix sum for the next num
            # only update if we haven't seen it before or found a smaller prefix sum
            if i+1<n:
                next_num = nums[i+1]
                if next_num not in min_prefix_before or min_prefix_before[next_num]>prefix_sum:
                    min_prefix_before[next_num] = prefix_sum
        return 0 if max_sum==float('-inf') else max_sum