class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k

        for digit in num:
            while k>0 and stack and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        res = ''.join(stack[:remain]).lstrip('0')
        return res