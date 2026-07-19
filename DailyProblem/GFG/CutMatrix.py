class Solution:
    def findWays(self, matrix, k):
        MOD = 10**9+7
        rows = len(matrix)
        cols = len(matrix[0])

        # suffix sum of ones
        suffix_ones = [[0]*(cols+1) for _ in range(rows+1)]
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                suffix_ones[r][c] = (
                    matrix[r][c]+suffix_ones[r+1][c]+suffix_ones[r][c+1]-suffix_ones[r+1][c+1]
                )
        if suffix_ones[0][0] < k:
            return 0
        
        # next valid horizontal cut
        next_row = [[rows]*cols for _ in range(rows)]
        for c in range(cols):
            for r in range(rows-1, -1, -1):
                if suffix_ones[r][c]>suffix_ones[r+1][c]:
                    next_row[r][c] = r+1
                elif r+1<rows:
                    next_row[r][c] = next_row[r+1][c]
        
        # next valid vertical cut
        next_col = [[cols]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols-1, -1, -1):
                if suffix_ones[r][c]>suffix_ones[r][c+1]:
                    next_col[r][c] = c+1
                elif c+1<cols:
                    next_col[r][c] = next_col[r][c+1]

        # base dp
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        for r in range(rows):
            for c in range(cols):
                dp[r][c]=1 if suffix_ones[r][c] else 0
        
        for pieces in range(2, k+1):
            row_suffix = [[0]*(cols+1) for _ in range(rows+1)]
            col_suffix = [[0]*(cols+1) for _ in range(rows+1)]

            for r in range(rows-1, -1, -1):
                for c in range(cols-1, -1, -1):
                    row_suffix[r][c] = (row_suffix[r+1][c]+dp[r][c])%MOD
                    col_suffix[r][c] = (col_suffix[r][c+1]+dp[r][c])%MOD
            
            curr = [[0]*(cols+1) for _ in range(rows+1)]
            for r in range(rows):
                for c in range(cols):
                    if suffix_ones[r][c]<pieces:
                        continue

                    ways = 0
                    if next_row[r][c]<rows+1:
                        ways += row_suffix[next_row[r][c]][c]
                    if next_col[r][c]<cols+1:
                        ways += col_suffix[r][next_col[r][c]]
                    curr[r][c] = ways%MOD
            dp = curr
        return dp[0][0]