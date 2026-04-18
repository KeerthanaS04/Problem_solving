class Solution:
    def maxOnes(self, arr):
        ans = 0
        zero = 0
        one = 0
        for num in arr:
            if num==0:
                zero+=1
            else:
                zero-=1
                one+=1
            ans = max(ans, zero)
            zero = max(zero, 0)
        return ans+one