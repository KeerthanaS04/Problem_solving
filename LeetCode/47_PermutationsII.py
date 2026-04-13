from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx: int) -> None:
            if idx==length:
                res.append(curr_per[:])
                return
            
            for j in range(length):
                if visited[j]:
                    continue

                # skip duplicate
                if j>0 and nums[j]==nums[j-1] and not visited[j-1]:
                    continue

                curr_per[idx] = nums[j]
                visited[j] = True
                backtrack(idx+1)
                visited[j] = False
        length = len(nums)
        nums.sort() # to group duplicates together
        res = []
        curr_per = [0]*length
        visited = [False]*length
        backtrack(0)
        return res