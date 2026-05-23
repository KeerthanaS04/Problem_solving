class Solution:
    def dfs(self, r, c, grid, vis):
        vis[r][c] = 1
        n = len(grid)
        m = len(grid[0])

        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        for k in range(4):
            nr = r+dr[k]
            nc = c+dr[k]

            if (0<=nr<n and 0<=nc<n and grid[nr][nc]==1 and not vis[nr][nc]):
                self.dfs(nr,nc,grid,vis)
    def cntOnes(self, grid):
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for _ in range(n)]

        # traverse first row and last row
        for j in range(m):
            if grid[0][j]==1 and not vis[0][j]:
                self.dfs(0,j,grid,vis)
            if grid[n-1][j]==1 and not vis[n-1][j]:
                self.dfs(n-1,j,grid,vis)
        
        # traverse first column and last column
        for i in range(n):
            if grid[i][0]==1 and not vis[i][0]:
                self.dfs(i,0,grid,vis)
            if grid[i][m-1]==1 and not vis[i][m-1]:
                self.dfs(i,m-1,grid,vis)
        
        cnt = 0

        # count all 1s that are not reachable from boundary
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    cnt+=1
        return cnt