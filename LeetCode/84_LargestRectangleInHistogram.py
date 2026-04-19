from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left_boundaries = [-1]*n
        right_boundaries = [n]*n

        for i, curr_height in enumerate(heights):
            while stack and heights[stack[-1]]>=curr_height:
                right_boundaries[stack[-1]] = i
                stack.pop()
            
            # the remaining top of stack is the left boundary for current element
            if stack:
                left_boundaries[i] = stack[-1]
            stack.append(i)
        max_area = max(height*(right_boundaries[i]-left_boundaries[i]-1) for i, height in enumerate(heights))
        return max_area