class Solution:
    def __init__(self):
        self.res = 0
    
    def helper(self, mat, i, j, r, c, ans):
        if i<0 or j<0 or i>=len(mat) or j>=len(mat[0]):
            return
        if mat[i][j] == 0 or mat[i][j]==-1:
            return
        
        if i==r and j==c:
            self.res = max(self.res, ans)
            return
        
        # mark visited
        mat[i][j] = -1

        self.helper(mat, i+1, j, r, c, ans+1)
        self.helper(mat, i-1, j, r, c, ans+1)
        self.helper(mat, i, j+1, r, c, ans+1)
        self.helper(mat, i, j-1, r, c, ans+1)

        # backtrack
        mat[i][j] = 0
    
    def longestPath(self, mat, xs, ys, xd, yd):
        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1
        
        self.res = 0
        self.helper(mat, xs, ys, xd, yd, 0)
        return self.res if self.res!=0 or (xs==xd and ys==yd) else -1