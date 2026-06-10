from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = []
        curr_start, curr_end = intervals[0]

        for int_start, int_end in intervals[1:]:
            if curr_end<int_start:
                merged_intervals.append([curr_start, curr_end])
                curr_start, curr_end = int_start, int_end
            else:
                curr_end = max(curr_end, int_end)
        
        # add the last interval to the last
        merged_intervals.append([curr_start, curr_end])
        return merged_intervals