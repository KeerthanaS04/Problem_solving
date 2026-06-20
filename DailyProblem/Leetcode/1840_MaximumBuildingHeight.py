from typing import List
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        height_restrictions = restrictions.copy()
        height_restrictions.append([1,0])
        height_restrictions.sort()

        # add the last position if already not present
        if not height_restrictions or height_restrictions[-1][0] != n:
            height_restrictions.append([n,n-1])
        num_restrictions = len(height_restrictions)

        # forward pass
        for i in range(1, num_restrictions):
            max_height_from_left = height_restrictions[i-1][1]+(height_restrictions[i][0]-height_restrictions[i-1][0])
            height_restrictions[i][1] = min(height_restrictions[i][1], max_height_from_left)
        
        # backward pass
        for i in range(num_restrictions-2, 0, -1):
            max_height_from_right = height_restrictions[i+1][1]+(height_restrictions[i+1][0]-height_restrictions[i][0])
            height_restrictions[i][1] = min(height_restrictions[i][1], max_height_from_right)
        
        # find the max possible height b/w consecutive restriction points
        max_height = 0
        for i in range(num_restrictions-1):
            # the formula finds the peak height when growing from both endpoints
            left_height = height_restrictions[i][1]
            right_height = height_restrictions[i+1][1]
            distance = height_restrictions[i+1][0]-height_restrictions[i][0]

            peak_height = (left_height+right_height+distance)//2
            max_height = max(max_height, peak_height)

        return max_height