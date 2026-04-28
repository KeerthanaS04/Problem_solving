class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        # if the string has odd length, it cannot form valid parentheses
        if (n&1): return False

        # left to right
        open_count = 0
        for i in range(n):
            if s[i]=='(' or locked[i]=='0':
                open_count+=1
            elif open_count>0:
                open_count-=1
            else:
                # too many closing parentheses
                return False
            
        # right to left
        close_count = 0
        for i in range(n-1, -1, -1):
            if s[i]==')' or locked[i]=='0':
                close_count+=1
            elif close_count>0:
                close_count-=1
            else:
                # too many parentheses that cannot be matched
                return False
        return True