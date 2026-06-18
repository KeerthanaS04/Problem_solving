class Solution:
    def findCoverage(self, mat):
        r = len(mat)
        c = len(mat[0])
        ans = 0

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    # left
                    for k in range(j-1, -1, -1):
                        if mat[i][k] == 1:
                            ans += 1
                            break
                    # right
                    for k in range(j+1, c):
                        if mat[i][k] == 1:
                            ans += 1
                            break
                    # up
                    for k in range(i-1, -1, -1):
                        if mat[k][j] == 1:
                            ans += 1
                            break
                    
                    # down
                    for k in range(i+1, r):
                        if mat[k][j] == 1:
                            ans += 1
                            break
        return ans