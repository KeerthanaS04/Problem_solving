from functools import cache
from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def dfs(curr_idx: int, last_jump: int) -> bool:
            # base case: reached the last stone
            if curr_idx==n-1:
                return True
            
            # try all possible jump distances: k-1, k, k+1
            for next_jump in range(last_jump-1, last_jump+2):
                target_pos = stones[curr_idx] + next_jump
                # check if there's a stone at the target position
                if next_jump>0 and target_pos in stone_pos_to_idx:
                    target_idx = stone_pos_to_idx[target_pos]
                    if dfs(target_idx, next_jump):
                        return True
            return False
        n = len(stones)
        stone_pos_to_idx = {pos: idx for idx, pos in enumerate(stones)}
        return dfs(0, 0)