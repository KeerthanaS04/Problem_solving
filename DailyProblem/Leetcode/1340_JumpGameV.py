from typing import List
from functools import cache
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @cache
        def dfs(idx: int) -> int:
            max_jump = 1

            # try jumping to the left
            for next_idx in range(idx-1, -1, -1):
                if idx-next_idx>d or arr[next_idx]>=arr[idx]:
                    break
                max_jump = max(max_jump, 1+dfs(next_idx))
            
            # try jumping to the right
            for next_idx in range(idx+1, n):
                if next_idx-idx>d or arr[next_idx]>=arr[idx]:
                    break
                max_jump = max(max_jump, 1+dfs(next_idx))
            return max_jump
        n = len(arr)
        return max(dfs(i) for i in range(n))