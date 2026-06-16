import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))

        while l<=r:
            curr_sum = l*l+r*r
            if curr_sum==c:
                return True
            elif curr_sum>c:
                r-=1
            else:
                l+=1
        return False