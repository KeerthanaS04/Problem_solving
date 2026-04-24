from typing import List
class Solution:
    def mostCompetition(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)

        for i, val in enumerate(nums):
            while stack and stack[-1]>val and len(stack)+n-i>k:
                stack.pop()
            if len(stack)<k:
                stack.append(val)
        return stack