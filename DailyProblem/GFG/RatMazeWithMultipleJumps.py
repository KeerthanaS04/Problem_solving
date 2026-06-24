class Solution:
    def shortestDist(self, mat):
        n = len(mat)
        if mat[0][0] == 0:
            return [[-1]]
        
        path = [[0]*n for _ in range(n)]
        bad = [[False]*n for _ in range(n)] # memoization

        def dfs(i, j):
            if i>=n or j>=n:
                return False
            if mat[i][j] == 0:
                return False
            if bad[i][j]:
                return False
            
            if i==n-1 and j==n-1:
                path[i][j] = 1
                return True
            path[i][j] = 1
            jump = mat[i][j]

            for step in range(1, jump+1):
                # right first
                if dfs(i, j+step):
                    return True
                # down second
                if dfs(i+step, j):
                    return True
            path[i][j] = 0
            bad[i][j] = True
            return False
        if dfs(0, 0):
            return path
        return [[-1]]