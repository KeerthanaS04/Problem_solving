class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0.0]*n for _ in range(n)] for _ in range(k+1)]

        # base case: 0 moves, knight is on the board
        for r in range(n):
            for c in range(n):
                dp[0][r][c] = 1.0
        # 8 possible moves of a knight
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        for moves in range(1, k+1):
            for r in range(n):
                for c in range(n):
                    for dr, dc in knight_moves:
                        prev_r, prev_c = r+dr, c+dc
                        if 0<=prev_r<n and 0<=prev_c<n:
                            dp[moves][r][c] += dp[moves-1][prev_r][prev_c]/8.0
        return dp[k][row][column]