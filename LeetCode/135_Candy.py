from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left_to_right = [1]*n
        right_to_left = [1]*n

        # left to right
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left_to_right[i] = left_to_right[i-1]+1
        
        # right to left
        for i in range(n-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                right_to_left[i] = right_to_left[i+1]+1
        
        # take maximum of both requirements
        total_candies = sum(max(left_candies, right_candies) for left_candies, right_candies in zip(left_to_right, right_to_left))
        return total_candies