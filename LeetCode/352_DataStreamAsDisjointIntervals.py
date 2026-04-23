from typing import List
from sortedcontainers import SortedDict
class SummaryRanges:
    def __init__(self):
        self.intervals_map = SortedDict()
    
    def addNum(self, val: int) -> None:
        num_intervals = len(self.intervals_map)

        right_idx = self.intervals_map.bisect_right(val)
        left_idx = num_intervals if right_idx==0 else right_idx-1

        # Get reference to keys and values for easier access
        interval_keys = self.intervals_map.keys()
        interval_values = self.intervals_map.values()

        # case 1: val connects two adjacent intervals (merging case)
        # check if val is exactly between two intervals (end of left+1==val==start of right-1)
        if (left_idx!=num_intervals and right_idx!=num_intervals and interval_values[left_idx][1]+1==val and interval_values[right_idx][0]-1==val):
            # merge the two intervals by extending the left interval to include the right
            self.intervals_map[interval_keys[left_idx]][1] = self.intervals_map[interval_keys[right_idx]][1]
            # remove the right interval as its now merged
            self.intervals_map.pop(interval_keys[right_idx])
        
        # case 2: val extends or is within the left interval
        elif left_idx!=num_intervals and val<=interval_values[left_idx][1]+1:
            # extend the end of the left interval if val is beyond it
            # if val is already within the interval, keep the curr end
            self.intervals_map[interval_keys[left_idx]][1] = max(val, self.intervals_map[interval_keys[left_idx]][1])

        # case 3: val extends or is at the beginning of the right interval
        elif right_idx!=num_intervals and val>=interval_values[right_idx][0]-1:
            # extend the start of the right interval to include val
            # use min to handle case where val might already be in the interval
            self.intervals_map[interval_keys[right_idx]][0] = min(val, self.intervals_map[interval_keys[right_idx]][0])
        
        # case 4: val creates a new isolated interval
        else:
            # create a new interval containing only val
            self.intervals_map[val] = [val, val]
    
    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals_map.values())