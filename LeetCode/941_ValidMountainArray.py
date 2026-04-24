from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        if n<3:
            return False
        
        left = 0
        right = n-1

        while left+1<n-1 and arr[left+1]>arr[left]:
            left+=1
        while right-1>0 and arr[right-1]>arr[right]:
            right-=1
        
        return left==right