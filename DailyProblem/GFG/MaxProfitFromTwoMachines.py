class Solution:
    def maxProfit(self, x, y, a, b):
        n = len(x)
        arr = []

        for i in range(n):
            arr.append((abs(a[i]-b[i]), i))
        arr.sort(reverse=True)
        ans = 0
        cntA = 0
        cntB = 0

        for diff, i in arr:
            if a[i]>=b[i]:
                if cntA < x:
                    ans += a[i]
                    cntA += 1
                else:
                    ans += b[i]
                    cntB += 1
            else:
                if cntB < y:
                    ans += b[i]
                    cntB += 1
                else:
                    ans += a[i]
                    cntA += 1
        return ans