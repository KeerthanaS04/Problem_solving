from typing import List
from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def calculate_score_diff(l: int, r: int) -> int:
            if l>r:
                return 0

            left_pick = piles[l]-calculate_score_diff(l+1, r)
            right_pick = piles[r]-calculate_score_diff(l, r-1)
            return max(left_pick, right_pick)

        return calculate_score_diff(0, len(piles)-1)>=0