class Solution:
    def minCandy(self, arr):
        n = len(arr)
        left_to_right = [1]*n
        right_to_left = [1]*n

        # left to right
        for i in range(1, n):
            if arr[i]>arr[i-1]:
                left_to_right[i] = left_to_right[i-1]+1
        
        # right to left
        for i in range(n-2, -1, -1):
            if arr[i]>arr[i+1]:
                right_to_left[i] = right_to_left[i+1]+1
        
        # take maximum of both the requirements
        total_candies = sum(max(left_candies, right_candies) for left_candies, right_candies in zip(left_to_right, right_to_left))
        return total_candies