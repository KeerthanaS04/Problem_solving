from typing import List
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        inc = [1]*(n+1)
        dec = [1]*(n+1)

        for i in range(2, n-1):
            if nums[i-1]<=nums[i-2]:
                dec[i] = dec[i-1]+1
        
        for i in range(n-3, -1, -1):
            if nums[i+1]<=nums[i+2]:
                inc[i] = inc[i+1]+1
        
        return [i for i in range(k, n-k) if dec[i]>=k and inc[i]>=k]