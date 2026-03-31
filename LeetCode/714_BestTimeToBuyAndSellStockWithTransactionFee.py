from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        pbs = -prices[0] # previous buy state
        pss = 0 # previous sell state

        for i in range(1, n):
            tbs = max(pbs, pss-prices[i])
            tss = max(pss, pbs+prices[i]-fee)

            pbs = tbs
            pss = tss
        return pss