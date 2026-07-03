from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_cost = 0
        curr_idx = 0
        n = len(colors)

        while curr_idx<n:
            group_start = curr_idx
            group_sum = 0
            max_time = 0

            while curr_idx<n and colors[curr_idx]==colors[group_start]:
                group_sum += neededTime[curr_idx]
                if max_time<neededTime[curr_idx]:
                    max_time = neededTime[curr_idx]
                curr_idx += 1
            
            # if group has more than one balloon, we need to remove all except one
            if curr_idx-group_start>1:
                total_cost += group_sum-max_time
        return total_cost