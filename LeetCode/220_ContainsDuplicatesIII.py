from typing import List
from sortedcontainers import SortedSet
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        sorted_window = SortedSet()

        for curr_idx, curr_val in enumerate(nums):
            lower_bound_idx = sorted_window.bisect_left(curr_val - valueDiff)

            if lower_bound_idx<len(sorted_window) and sorted_window[lower_bound_idx]<=curr_val + valueDiff:
                return True
            
            sorted_window.add(curr_val)
            if curr_idx>=indexDiff:
                sorted_window.remove(nums[curr_idx-indexDiff])
        return False