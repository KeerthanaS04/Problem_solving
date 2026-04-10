class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_res = 0
        curr_sign = 1
        idx = 0
        n = len(s)

        while idx<n:
            char = s[idx]
            if char.isdigit():
                num = 0
                digit_start = idx

                # continue reading digits to form the complete number
                while idx<n and s[digit_start].isdigit():
                    num = num*10+int(s[digit_start])
                    digit_start += 1
                curr_res += curr_sign*num
                idx = digit_start-1
            elif char=='+':
                curr_sign = 1
            elif char=='-':
                curr_sign = -1
            elif char=='(':
                # handling parenthesis
                stack.append(curr_res)
                stack.append(curr_sign)

                # reset for new expression inside parenthesis
                curr_res = 0
                curr_sign = 1
            elif char==')':
                prev_sign = stack.pop()
                prev_res = stack.pop()

                curr_res = prev_sign*curr_res+prev_res
            idx += 1
        return curr_res