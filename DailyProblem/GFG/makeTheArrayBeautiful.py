class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        res = []

        for x in arr:
            if res and ((res[-1]<0 and x>=0) or (res[-1]>=0 and x<0)):
                res.pop()
            else:
                res.append(x)
        return res