from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index: int) -> int:
            if index>=n:
                result.append(curr_per[:])
                return
            for j, num in enumerate(nums):
                if not used[j]:
                    used[j] = True
                    curr_per[index] = num
                    backtrack(index+1)
                    used[j] = False
        n = len(nums)
        used = [False]*n
        curr_per = [0]*n
        result = []

        backtrack(0)
        return result