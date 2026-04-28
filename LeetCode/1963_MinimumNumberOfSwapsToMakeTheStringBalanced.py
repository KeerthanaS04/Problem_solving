class Solution:
    def minSwaps(self, s: str) -> int:
        unmatched_open = 0

        for c in s:
            if c=='[':
                unmatched_open+=1
            elif unmatched_open>0:
                unmatched_open-=1
        return (unmatched_open+1)//2