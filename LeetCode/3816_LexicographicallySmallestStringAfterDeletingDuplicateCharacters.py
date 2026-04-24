from collections import Counter
class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        cnt = Counter()
        stack = []
        
        for char in s:
            while stack and stack[-1]>char and cnt[stack[-1]]>1:
                cnt[stack.pop()]-=1
            stack.append(char)
        
        while stack and cnt[stack[-1]]>1:
            cnt[stack.pop()]-=1
        return ''.join(stack)