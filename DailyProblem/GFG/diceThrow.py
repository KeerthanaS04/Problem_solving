class Solution:
    def __init(self):
        self.dp = [[-1]*51 for _ in range(51)]
    
    def solve(self, m, n, x):
        if x<0:
            return 0
        
        if self.dp[n][x]!=-1:
            return self.dp[n][x]
        if n==0 and x==0:
            return 1
        if n==0:
            return 0
        result = 0

        for face in range(1, m+1):
            result+=self.solve(m, n-1, x-face)
        self.dp[n][x] = result
        return result
    
    def noOfWays(self, m, n, x):
        self.dp = [[-1]*51 for _ in range(51)]
        return self.solve(m, n, x)