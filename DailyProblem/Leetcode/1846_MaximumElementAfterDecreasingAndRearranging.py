from typing import List
class Solution:
    def maximumElementAfterDecreasingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            diff = max(0, arr[i] - arr[i-1]-1)
            arr[i]-=diff
        return max(arr)