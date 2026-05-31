class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        return n&(n-1)!=0