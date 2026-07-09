from collections import defaultdict

class Solution:
    def countKdivPairs(self, arr, k):
        mp = defaultdict(int)
        ans = 0

        for num in arr:
            rem = num % k
            ans += mp[rem]
            mp[(k-rem)%k] += 1
        return ans