class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_par = {'()', '{}', '[]'}

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack or stack.pop()+char not in valid_par:
                    return False
        return not stack