from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx: int) -> None:
            if idx==len(nums):
                res.append(curr_subset[:])
                return 
            
            # exclude the curr element
            dfs(idx+1)
            # include the curr element
            curr_subset.append(nums[idx])
            dfs(idx+1)

            # remove the ele we just added
            curr_subset.pop()
        res = []
        curr_subset = []
        dfs(0)
        return res