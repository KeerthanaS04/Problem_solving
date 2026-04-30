from typing import List
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # the sum of first i elements in the jth column
        prefix = [[0]*(n+1) for _ in range(n)]
        # the maximum score upto the prev column, where the bottommost selected element in the prev column is in row(i-1)
        prevPick = [0]*(n+1)
        # the maximum score upto the prev column, where the bottommost selected element in the column before the prev one is in row (i-1)
        prevSkip = [0]*(n+1)

        for j in range(n):
            for i in range(n):
                prefix[j][i+1] = prefix[j][i]+grid[i][j]
        
        for j in range(1,n):
            currPick = [0]*(n+1)
            currSkip = [0]*(n+1)

            for curr in range(n+1): # the no of curr selected elements
                for prev in range(n+1): # the no of prev selected elements
                    if curr>prev:
                        # the prev bottom is deeper than curr bottom
                        score = prefix[j-1][curr] - prefix[j-1][prev]
                        currPick[curr] = max(currPick[curr], prevSkip[prev]+score)
                        currSkip[curr] = max(currSkip[curr], prevPick[prev]+score)
                    else:
                        score = prefix[j][prev] - prefix[j][curr]
                        currPick[curr] = max(currPick[curr], prevSkip[prev]+score)
                        currSkip[curr] = max(currSkip[curr], prevPick[prev])
            prevPick = currPick
            prevSkip = currSkip
        return max(prevPick)