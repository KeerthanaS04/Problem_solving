class Solution:
    def countBTS(self, arr):
        n = len(arr)
        MOD = 10**9+7

        # catalan number - number of unique BSTs with k nodes
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for k in range(1, i+1):
                dp[i] = (dp[i]+dp[k-1]*dp[i-k])%MOD
        
        # sort and map values to indices
        temp = arr[:]
        arr.sort()
        mp = {}
        for i in range(n):
            mp[arr[i]] = i
        ans = [0]*n
        for i in range(n):
            e = temp[i]
            left = mp[e]
            right = n-mp[e]-1
            ans[i] = (dp[left]*dp[right])%MOD
        return ans