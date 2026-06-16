class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for char in s:
            if char.isalpha():
                res.append(char)
            elif char=='*' and res:
                res.pop()
            elif char=='#':
                res.extend(res[:])
            elif char=='%':
                res.reverse()
        return ''.join(res)