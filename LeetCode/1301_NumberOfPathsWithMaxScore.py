from typing import List
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        dp = [[-1] * (n+1) for _ in range(n+1)]
        count = [[0] * (n+1) for _ in range(n+1)]

        dp[n-1][n-1] = 0
        count[n-1][n-1] = 1
        # from top left to bottom right
        directions = [(1,0), (0,1), (1,1)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] in ('X', 'S'):
                    continue

                for dx, dy in directions:
                    ni, nj = i+dx, j+dy
                    if dp[ni][nj]>dp[i][j]:
                        dp[i][j] = dp[ni][nj]
                        count[i][j] = count[ni][nj]
                    elif dp[ni][nj]==dp[i][j]:
                        count[i][j] = (count[i][j] + count[ni][nj]) % MOD
                
                if board[i][j]!='E' and dp[i][j]!=-1:
                    dp[i][j] += int(board[i][j])
        
        if dp[0][0]==-1:
            return [0, 0]
        return [dp[0][0], count[0][0]]