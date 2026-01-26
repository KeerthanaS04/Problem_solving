from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        mini = float('inf')
        for i in range(1, n):
            mini = min(mini, arr[i]-arr[i-1])
        
        result = []
        for i in range(1, n):
            if arr[i]-arr[i-1]==mini:
                result.append([arr[i-1], arr[i]])
        return result