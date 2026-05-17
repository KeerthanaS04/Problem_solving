class Solution:
    def findSmallest(self, arr):
        arr.sort()
        ans = 1

        for x in arr:
            if x>ans:
                return ans
            ans+=x
        return ans