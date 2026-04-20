from typing import List
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0
        n = len(colors)

        for i in range(n):
            for j in range(i+1, n):
                if colors[i]!=colors[j]:
                    max_dist = max(max_dist, abs(i-j))
        return max_dist