from itertools import accumulate
from functools import cache
from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def dp(start_idx: int, max_take: int) -> int:
            if max_take*2>=total_piles-start_idx:
                return prefix_sum[total_piles]-prefix_sum[start_idx]

            # current player's score = total remaining stones - opponent's score
            max_stones = 0
            for num_piles in range(1, 2*max_take+1):
                stones_obt = prefix_sum[total_piles] - prefix_sum[start_idx]-dp(start_idx+num_piles, max(max_take, num_piles))
                max_stones = max(max_stones, stones_obt)
            return max_stones

        total_piles = len(piles)
        prefix_sum = list(accumulate(piles, initial=0))
        return dp(0, 1)