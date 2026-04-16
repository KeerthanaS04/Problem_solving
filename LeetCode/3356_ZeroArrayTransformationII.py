from typing import List
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total_queries = len(queries)

        def feasible(k: int) -> bool:
            diff_arr = [0]*(n+1)

            for i in range(k):
                l, r, val = queries[i]
                diff_arr[l]+=val
                diff_arr[r+1]-=val
            cum_sum = 0
            for i in range(n):
                cum_sum+=diff_arr[i]

                if nums[i]>cum_sum:
                    return False
            return True
        
        l, r = 0, total_queries
        first_true_idx = -1
        while l<=r:
            mid = (l+r)//2
            if feasible(mid):
                first_true_idx = mid
                r = mid-1
            else:
                l = mid+1
        return first_true_idx