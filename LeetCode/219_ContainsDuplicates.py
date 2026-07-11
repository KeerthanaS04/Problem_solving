from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for curr_idx, val in enumerate(nums):
            if val in index_map and curr_idx - index_map[val] <= k:
                return True
            index_map[val] = curr_idx
        return False