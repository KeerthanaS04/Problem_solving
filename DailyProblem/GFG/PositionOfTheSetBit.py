import math
class Solution:
    def findPosition(self, n):
        # check if n has exactly one bit
        if n<=0 or (n&(n-1))!=0:
            return -1
        return int(math.log2(n))+1