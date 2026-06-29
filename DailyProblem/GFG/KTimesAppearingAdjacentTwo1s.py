from functools import lru_cache
class Solution:
    def countStrings(self, n, k):
        MOD = 10**9+7
        @lru_cache(None)
        def solve(i, count, prev):
            if count>k:
                return 0
            if i==n:
                return 1 if count==k else 0
            
            # place '0'
            ans = solve(i+1, count, 0)
            # place '1'
            ans = (ans+solve(i+1, count+(prev==1), 1))%MOD
            return ans
        return (solve(1,0,0)+solve(1,0,1))%MOD