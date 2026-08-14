class Solution:
    def zigzagSequence(self, mat):
        n = len(mat)

        for i in range(1, n):
            for j in range(n):
                mx = 0

                for k in range(n):
                    if j==k:
                        continue
                    mx = max(mx, mat[i-1][k])
                mat[i][j] += mx
        res = 0
        for j in range(n):
            res = max(res, mat[n-1][j])
        return res