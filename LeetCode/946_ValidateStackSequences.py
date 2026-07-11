from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_idx = 0

        for push_val in pushed:
            stack.append(push_val)

            while stack and stack[-1]==popped[pop_idx]:
                stack.pop()
                pop_idx += 1
        return pop_idx==len(popped)