from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(row: int, col: int) -> None:
            # check if curr cell is 'O' and within boundaries
            if not (0<=row<rows and 0<=col<cols and board[row][col]=='O'):
                return
            
            # mark current cell as visited
            board[row][col]='.'
            directions = [(-1,0),(0,1),(1,0),(0,-1)]
            for dx, dy in directions:
                dfs(row+dx, col+dy)
            
        # check left and right borders
        for row in range(rows):
            dfs(row,0)
            dfs(row,cols-1)
        
        # check top and bottom borders
        for col in range(cols):
            dfs(0,col)
            dfs(rows-1,col)
        
        # convert all cells based on their curr state
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=='.':
                    board[row][col]='O'
                elif board[row][col]=='O':
                    board[row][col]='X'