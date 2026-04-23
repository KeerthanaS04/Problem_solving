from typing import List
from bisect import bisect_left
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        res = [-1]*n

        sorted_starts = sorted((start, idx) for idx, (start, _) in enumerate(intervals))

        for idx, (_, end) in enumerate(intervals):
            # binary search for the first interval whose start>=current interval's end
            pos = bisect_left(sorted_starts, (end, float('-inf')))

            if pos<n:
                res[idx] = sorted_starts[pos][1]
        return res