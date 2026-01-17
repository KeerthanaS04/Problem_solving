class Solution:
    def is_operator(self, ch):
        return ch in ['+', '-', '*', '/']
    def checkRedundancy(self, s):
        stack = []

        for ch in s:
            if ch=='(':
                stack.append(['(', 0])
            elif self.is_operator(ch):
                if stack:
                    stack[-1][1]+=1
            elif ch==')':
                if not stack:
                    return True
                else:
                    if stack[-1][1]==0:
                        return True
                    else:
                        stack.pop()
        return False