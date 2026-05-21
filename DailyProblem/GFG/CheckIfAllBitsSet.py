class Solution:
    def isBitSet(self, n):
        if n==0:
            return False
        return ((n+1)&n)==0