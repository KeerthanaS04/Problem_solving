from typing import List
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        max_jump_dist = stones[1]-stones[0]

        for i in range(2, len(stones)):
            max_jump_dist = max(max_jump_dist, stones[i]-stones[i-2])
        return max_jump_dist