class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        total_score = 0
        depth = 0

        for idx, char in enumerate(s):
            if char=='(':
                depth+=1
            else:
                depth-=1

                # check if this closing parentheses forms () pattern
                if s[idx-1]=='(':
                    total_score+=1<<depth
        
        return total_score