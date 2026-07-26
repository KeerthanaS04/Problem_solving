class Solution:
    def maximumSum(self, mat, k):
        n = len(mat)

        # build prefix sum matrix
        prefix = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(n):
                prefix[i+1][j+1] = (
                    mat[i][j]+prefix[i][j+1]+prefix[i+1][j]-prefix[i][j]
                )

        max_sum = float("-inf")

        # check for every k x k sub-matrix
        for i in range(n-k+1):
            for j in range(n-k+1):
                curr_sum = (
                    prefix[i+k][j+k]-prefix[i][j+k]-prefix[i+k][j]+prefix[i][j]
                )
                max_sum = max(max_sum, curr_sum)
        return max_sum