def guess(num: int) -> int:
    return num
class Solution:
    def guessNumber(self, n: int) -> int:
        def feasible(mid: int) -> bool:
            return guess(mid)<=0

        l, r = 1, n
        first_true_idx = -1
        while l<=r:
            mid = (l+r)//2
            if feasible(mid):
                first_true_idx = mid
                r = mid-1
            else:
                l = mid+1
        return first_true_idx