class Solution:
    def divisibleByK(self, arr, k):
        dp = [False]*k

        for num in arr:
            temp = dp[:]
            temp[num%k] = True

            for rem in range(k):
                if dp[rem]:
                    temp[(rem + num) % k] = True
            
            dp = temp
            if dp[0]:
                return True
        return False