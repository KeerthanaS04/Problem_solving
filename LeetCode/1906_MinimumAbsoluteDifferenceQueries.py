from typing import List
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        num_elements = len(nums)
        num_queries = len(queries)
        MAX_VAL = 100
        prefix_count = [[0]*(MAX_VAL+1) for _ in range(num_elements+1)]

        # calculate prefix counts for each number
        for i in range(num_elements):
            for val in range(1, MAX_VAL+1):
                prefix_count[i][val] = prefix_count[i-1][val]
                if nums[i-1] == val:
                    prefix_count[i][val] += 1
        res = []
        for query_idx in range(num_queries):
            l = queries[query_idx][0]
            r = queries[query_idx][1]+1
            min_diff = float('inf')
            prev_val = -1

            for val in range(1, MAX_VAL+1):
                count_in_range = prefix_count[r][val] - prefix_count[l][val]
                if count_in_range > 0:
                    if prev_val != -1:
                        min_diff = min(min_diff, val - prev_val)
                    prev_val = val
            if min_diff == float('inf'):
                min_diff = -1
            res.append(min_diff)
        return res