from typing import List
from heapq import heappush, heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        num_intervals = len(intervals)
        num_queries = len(queries)

        intervals.sort()
        indexed_queries = sorted((val, idx) for idx, val in enumerate(queries))
        res = [-1]*num_queries
        min_heap = []
        # pointer to track which interval we are currently processing
        interval_idx = 0

        for query_val, idx in indexed_queries:
            while interval_idx<num_intervals and intervals[interval_idx][0]<=query_val:
                start, end = intervals[interval_idx]
                interval_size = end-start+1
                heappush(min_heap, (interval_size, end))
                interval_idx+=1
            
            # remove intervals from heap that end before the current query point
            while min_heap and min_heap[0][1]<query_val:
                heappop(min_heap)

            if min_heap:
                res[idx] = min_heap[0][0]
        return res