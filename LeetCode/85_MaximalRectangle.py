from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        num_cols = len(matrix[0])
        heights = [0]*num_cols
        max_area = 0

        for row in matrix:
            for col_idx, value in enumerate(row):
                if value=='1':
                    heights[col_idx]+=1
                else:
                    heights[col_idx] = 0
                max_area = max(max_area, self.largestRectangle(heights))
        return max_area
    
    def largestRectangle(self, heights: List[List[int]]) -> int:
        n = len(heights)
        left_boundaries = [-1]*n
        right_boundaries = [n]*n
        stack = []

        # calculate left boundaries
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            #if stack is not empty, then the top element is the nearest smaller on the left
            if stack:
                left_boundaries[i] = stack[-1]
            stack.append(i)

        stack=[]
        # calculate right boundaries
        for i in range(n-1, -1, -1):
            if stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                right_boundaries[i] = stack[-1]
            stack.append(i)
        
        max_area = max(height*(right_boundaries[i]-left_boundaries[i]-1) for i, height in enumerate(heights))
        return max_area