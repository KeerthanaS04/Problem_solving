from typing import List
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group_id = [0] * n
        curr_group = 0

        for i in range(1, n):
            # check if difference between consecutive elements exceeds maxDiff
            if nums[i] - nums[i - 1] > maxDiff:
                curr_group += 1
            group_id[i] = curr_group

        # for each query [u,v], check if both indices are in the same group
        res = [group_id[u] == group_id[v] for [u, v] in queries]
        return res