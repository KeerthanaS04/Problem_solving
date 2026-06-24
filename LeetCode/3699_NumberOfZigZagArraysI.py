class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1_000_000_007
        r-=l
        dp = [1]*(r+1)

        for i in range(1, n):
            pre = 0

            if i&1: # odd index
                for v in range(r+1):
                    pre2 = pre+dp[v]
                    dp[v] = pre
                    pre = pre2%MOD

            else: # even index
                for v in range(r, -1, -1):
                    pre2 = pre+dp[v]
                    dp[v] = pre
                    pre = pre2%MOD
        res = sum(dp)%MOD
        return res*2%MOD