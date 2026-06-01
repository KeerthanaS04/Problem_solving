from typing import List
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = sum(cost)-sum(cost[2::3])
        return total