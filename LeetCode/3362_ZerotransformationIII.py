from typing import List
from heapq import heappush, heappop
class Solution:
    def maxRemoval(self, nums: list[int], queries: List[List[int]]) -> int:
        queries.sort()
        diff_arr = [0]*(len(nums)+1)
        queries_heap = []
        curr_coverage = 0
        query_idx = 0

        for pos, req_val in enumerate(nums):
            curr_coverage+=diff_arr[pos]

            while query_idx<len(queries) and queries[query_idx][0]<=pos:
                heappush(queries_heap, -queries[query_idx][1])
                query_idx+=1
            
            while curr_coverage<req_val and queries_heap and -queries_heap[0]>=pos:
                curr_coverage+=1
                query_end_pos = -heappop(queries_heap)
                diff_arr[query_end_pos+1]-=1
            
            if curr_coverage<req_val:
                return -1
        return len(queries_heap)