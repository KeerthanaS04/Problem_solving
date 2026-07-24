class Solution:
    def canRepresentBST(self, arr):
        stack = []
        limit = float('-inf')

        for x in arr:
            if x<limit:
                return False
            while stack and x>stack[-1]:
                limit = stack.pop()
            stack.append(x)
        return True