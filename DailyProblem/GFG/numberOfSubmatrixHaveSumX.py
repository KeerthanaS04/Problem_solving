class Solution:
    def countSquare(self, mat, x):
        n = len(mat)
        m = len(mat[0])

        # Build the prefix
        prefix = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):
                prefix[i+1][j+1] = mat[i][j]+prefix[i+1][j]+prefix[i][j+1]-prefix[i][j]

        count = 0
        for k in range(1, min(n, m)+1):
            for i in range(k, n+1):
                for j in range(k, m+1):
                    total = prefix[i][j] - prefix[i-k][j] - prefix[i][j-k]+prefix[i-k][j-k]

                    if total==x:
                        count+=1
        return count