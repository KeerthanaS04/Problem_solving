from typing import List
from functools import cache
from math import inf
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def dfs(idx: int) -> int:
            if idx>=n:
                return 0

            max_score_diff = -inf
            curr_sum = 0

            for num_stones in range(3):
                if num_stones + idx >= n:
                    break
                curr_sum += stoneValue[idx + num_stones]
                score_diff = curr_sum - dfs(idx + num_stones + 1)
                max_score_diff = max(max_score_diff, score_diff)
            return max_score_diff

        n = len(stoneValue)
        alice_score_diff = dfs(0)

        if alice_score_diff==0:
            return "Tie"
        elif alice_score_diff>0:
            return "Alice"
        else:
            return "Bob"