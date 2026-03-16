from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(l: int, r: int, curr: str):
            if l>n or r>n or r>l:
                return
            if l==n and r==n:
                result.append(curr)
                return
            backtrack(l+1,r,curr+'(')
            backtrack(l,r+1,curr+')')
        result = []
        backtrack(0,0,'')
        return result