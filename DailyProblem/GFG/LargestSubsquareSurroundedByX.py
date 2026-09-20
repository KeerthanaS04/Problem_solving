class Solution:
    def largestSubsquare(self, mat):
        n = len(mat)
        right = [[0]*n for _ in range(n)]
        down = [[0]*n for _ in range(n)]

        # calculate consecutive 'X's to the right and down for each cell
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] == 'X':
                    right[i][j] = 1
                    down[i][j] = 1

                    if j+1 < n:
                        right[i][j] += right[i][j+1]
                    if i+1 < n:
                        down[i][j] += down[i+1][j]

        ans = 0
        for i in range(n):
            for j in range(n):
                maxSize = min(right[i][j], down[i][j])

                for k in range(maxSize, ans, -1):
                    bottom = i+k-1
                    rightCol = j+k-1

                    if right[bottom][j]>=k and down[i][rightCol]>=k:
                        ans = k
                        break
        return ans