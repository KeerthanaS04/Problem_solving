from typing import List
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        sorted_pairs = sorted(zip(nums, cost))
        n = len(sorted_pairs)

        # sum of (number*cost)
        prefix_weighted_sum = [0]*(n+1)
        prefix_cost_sum = [0]*(n+1)

        for i in range(1, n+1):
            num_val, cost_val = sorted_pairs[i-1]
            prefix_weighted_sum[i] = prefix_weighted_sum[i-1]+num_val*cost_val
            prefix_cost_sum[i] = prefix_cost_sum[i-1]+cost_val

        min_total_cost = float('inf')

        # target each pos as the target point
        for i in range(1, n+1):
            target_num = sorted_pairs[i-1][0]

            # cost to move all the elements on the left to target num
            left_cost = target_num*prefix_cost_sum[i-1]-prefix_weighted_sum[i-1]
            right_cost = (prefix_weighted_sum[n]-prefix_weighted_sum[i]) - target_num*(prefix_cost_sum[n]-prefix_cost_sum[i])
            min_total_cost = min(min_total_cost, left_cost+right_cost)
        return min_total_cost