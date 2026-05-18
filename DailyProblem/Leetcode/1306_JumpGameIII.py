from typing import List
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])

        while queue:
            curr_idx = queue.popleft()
            if arr[curr_idx]==0:
                return True
            jump_dist = arr[curr_idx]
            arr[curr_idx] = -1

            # check for both possible: forward and backward
            for next_idx in (curr_idx+jump_dist, curr_idx-jump_dist):
                if 0<=next_idx<len(arr) and arr[next_idx]>=0:
                    queue.append(next_idx)
        return False