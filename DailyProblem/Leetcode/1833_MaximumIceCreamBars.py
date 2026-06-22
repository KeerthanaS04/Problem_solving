from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        for idx, cost in enumerate(costs):
            if coins<cost:
                return idx
            coins-=cost
        return len(costs)