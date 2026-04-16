from typing import List
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # to handle circular array logic
        double_length = n*2
        min_distances = [double_length]*double_length

        # left to right
        # track the last seen position of each value
        last_pos_left = {}
        for i in range(double_length):
            curr_val = nums[i%n]

            if curr_val in last_pos_left:
                min_distances[i] = min(min_distances[i], i-last_pos_left[curr_val])
            last_pos_left[curr_val] = i
        
        # right to left
        # track the next seen position of each value
        next_pos_right = {}
        for i in range(double_length, -1, -1):
            curr_val = nums[i%n]

            if curr_val in next_pos_right:
                min_distances[i] = min(min_distances[i], next_pos_right[curr_val]-i)
            next_pos_right[curr_val] = i
        
        for i in range(n):
            min_distances[i] = min(min_distances[i], min_distances[i+n])
        return [-1 if min_distances[query_idx]>=n else min_distances[query_idx] for query_idx in queries]