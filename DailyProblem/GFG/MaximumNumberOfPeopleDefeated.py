class Solution:
    def maxPeopleDefeated(self, p):
        l, r = 0, 10000
        ans = 0

        while l<=r:
            mid = l+(r-l)//2
            total = mid*(mid+1)*(2*mid+1)//6

            if total<=p:
                ans = mid
                l = mid+1
            else:
                r = mid-1

        return ans