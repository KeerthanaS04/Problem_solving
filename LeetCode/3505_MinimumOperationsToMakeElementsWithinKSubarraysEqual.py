from bisect import bisect_left, insort
from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        minOps = self.getMinOps(nums, x)
        n = len(nums)
        mem = [[-1]*(k+1) for _ in range(n+1)]
        return self.dp(nums,x,0,k,minOps, mem)
    
    def dp(self, nums, x, i, k, minOps, mem):
        if k==0:
            return 0
        if i==len(nums):
            return float('inf')
        if mem[i][k]!=-1:
            return mem[i][k]
        
        # two choices: skip or pick
        skip = self.dp(nums, x, i+1, k, minOps, mem)
        pick = float('inf')
        if i+x<=len(nums):
            pick = minOps[i]+self.dp(nums, x, i+x, k-1, minOps, mem)
        nums[i][k] = min(skip, pick)
        return mem[i][k]
    
    def getMinOps(self, nums, x):
        lower = [] # max side sorted
        upper = [] # min side sorted
        lowerSum = 0
        upperSum = 0
        minOps = []

        for i in range(len(nums)):
            # insert into correct half
            if not lower or nums[i]<=lower[-1]:
                insort(lower, nums[i])
                lowerSum+=nums[i]
            else:
                insort(upper, nums[i])
                upperSum+=nums[i]
            
            # remove element out of window
            if i>=x:
                out = nums[i-x]
                idx = bisect_left(lower, out)
                if idx<len(lower) and lower[idx]==out:
                    lower.pop(idx)
                    lowerSum-=out
                else:
                    idx = bisect_left(upper, out)
                    upper.pop(idx)
                    upperSum-=out
            
            # balance
            if len(lower)<len(upper):
                val = upper.pop()
                upperSum-=val
                insort(lower, val)
                lowerSum+=val
            elif len(lower)-len(upper)>1:
                val = lower.pop()
                lowerSum-=val
                insort(upper, val)
                upperSum+=val
            
            # compute cost
            if i>=x-1:
                median = lower[-1]
                ops = (median*len(lower)-lowerSum) + (upperSum-median*len(upper))
                minOps.append(ops)
        return minOps