from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i in range(len(prices), -1, -1):
            curr_price = prices[i]

            while stack and curr_price<stack[-1]:
                stack.pop()
            
            if stack:
                prices[i]-=stack[-1]
            stack.append(i)
        return prices