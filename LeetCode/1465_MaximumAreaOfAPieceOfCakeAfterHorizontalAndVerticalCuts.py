from typing import List
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0,h])
        verticalCuts.extend([0,w])

        horizontalCuts.sort()
        verticalCuts.sort()

        max_height = 0
        for i in range(1, len(horizontalCuts)):
            max_height = max(max_height, horizontalCuts[i]-horizontalCuts[i-1])

        max_width = 0
        for i in range(1, len(verticalCuts)):
            max_width = max(max_width, verticalCuts[i]-verticalCuts[i-1])

        MOD = 10**9+7
        return (max_height*max_width)%MOD