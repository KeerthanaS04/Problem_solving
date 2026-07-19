from typing import List
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        left = [1]*n
        right = [1]*n

        for i in range(1, n):
            if arr[i]>arr[i-1]:
                left[i] = left[i-1]+1
        max_length = 0
        for i in range(n-2, -1, -1):
            if arr[i]>arr[i+1]:
                right[i] = right[i+1]+1

                if left[i]>1:
                    max_length = max(max_length, left[i]+right[i]-1)
        return max_length