class Solution:
    def minCost(self, heights, cost):
        # combine heights and cost
        arr = sorted(zip(heights, cost))

        total = sum(cost)
        curr = 0

        # Find weighted median
        for h, c in arr:
            curr+=c
            if curr>=total/2:
                target = h
                break
        
        # Calculate total cost using weighted median
        ans = 0
        for h, c in arr:
            ans+=abs(h-target)*c
        
        return ans