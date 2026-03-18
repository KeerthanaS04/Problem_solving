class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0
        consecutiveOnes = 0

        while n>0:
            if n&1:
                consecutiveOnes+=1
            elif consecutiveOnes>0:
                # processing the groups of 1s
                operations+=1
                # reset the counter if we had escatly one 1, otherwise carry over 1
                consecutiveOnes=0 if consecutiveOnes==1 else 1
            n>>=1
        if consecutiveOnes==1:
            operations+=1
        elif consecutiveOnes>1:
            operations+=2
        return operations