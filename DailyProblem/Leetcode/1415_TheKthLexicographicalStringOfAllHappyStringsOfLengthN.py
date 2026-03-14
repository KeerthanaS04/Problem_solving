class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(curr: list[str], res: list[str]) -> None:
            # base case
            if len(curr)==n:
                res.append(''.join(curr))
                return
            if len(res)>=k:
                return
            
            for char in 'abc':
                if not curr or curr[-1]!=char:
                    curr.append(char)
                    backtrack(curr, res)
                    curr.pop()
        all_happy_strings = []
        curr_build = []

        backtrack(curr_build, all_happy_strings)
        return "" if len(all_happy_strings)<k else all_happy_strings[k-1]