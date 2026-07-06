from typing import List
import math
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals by start time (ascending)
        # if start times are the same, sort by end time (descending)
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        non_covered_count = 0
        max_end_point = -math.inf

        for start, end in intervals:
            if end > max_end_point:
                max_end_point = end
                non_covered_count += 1
        return non_covered_count