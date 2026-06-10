from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mini  = float('inf')
        for i in range(1, len(arr)):
            mini = min(mini, arr[i]-arr[i-1])
        
        res = []
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] == mini:
                res.append([arr[i-1], arr[i]])
        return res