class Solution:
    MOD = 1000000007
    def computeValue(self, n):
        # first half can be C(n, k), where it contains exactly k ones and same for the second half
        # therefore for a fixed k, c(n, k)^2
        # so total answer is sum of (c(n,k)^2)
        ans = 1
        # compute c(2n,n)
        for i in range(1, n+1):
            ans = (ans*(2*n-i+1))%self.MOD

            # divide i by using modular inverse
            ans = (ans*(self.power(i, self.MOD-2)))%self.MOD
        return ans
    
    def power(self, a, b):
        res = 1
        while b > 0:
            if b & 1:
                res = (res*a)%self.MOD
            a = (a*a)%self.MOD
            b >>= 1
        return res