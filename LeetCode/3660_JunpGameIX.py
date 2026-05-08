from typing import List
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        pre_max = [nums[0]]*n
        for i in range(1,n):
            pre_max[i] = max(pre_max[i-1], nums[i])
        
        suff_min = float('inf')
        for i in range(n-1, -1, -1):
            if i+1<n:
                ans[i] = ans[i+1] if pre_max[i]>suff_min else pre_max[i]
            else:
                ans[i] = pre_max[i] if pre_max<=suff_min else 0
            suff_min = min(suff_min, nums[i])
        return ans