from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx: int):
            if idx==len(nums):
                res.append(curr_subset[:])
                return
            
            # include the curr element
            curr_subset.append(nums[idx])
            dfs(idx+1)

            # remove the element we added
            removed_ele = curr_subset.pop()

            # skip all duplicates of the removed ele
            while idx+1<len(nums) and nums[idx+1]==removed_ele:
                idx+=1
            
            # exclude the curr element
            dfs(idx+1)
        nums.sort()
        res = []
        curr_subset = []
        dfs(0)
        return res