class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        open_count = 0

        # remove invalid ) paretheses
        for char in s:
            if char==')' and open_count==0:
                continue

            # track the count
            if char=='(':
                open_count+=1
            elif char==')':
                open_count-=1
            stack.append(char)
        
        result = []
        close_count = 0

        # remove invalid ( parenthese 
        for char in reversed(stack):
            if char=='(' and close_count==0:
                continue

            # track the count
            if char==')':
                close_count+=1
            elif char=='(':
                close_count-=1
            result.append(char)
        return ''.join(reversed(result))