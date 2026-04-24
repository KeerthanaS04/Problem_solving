class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        stack = []
        required = repetition
        nLetters = s.count(letter)

        for i in range(len(s)):
            c = s[i]

            while stack and stack[-1]>c and len(s)+len(stack)>=k and (stack[-1]!=letter or nLetters>required):
                popped = stack.pop()
                if popped==letter:
                    required+=1
            
            if len(stack)<k:
                if c==letter:
                    stack.append(c)
                    required-=1
                elif k>len(stack)+required:
                    stack.append(c)
            if c==letter:
                nLetters-=1
        return ''.join(stack)