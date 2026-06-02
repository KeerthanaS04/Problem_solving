class Solution:
    def sumDiffPairs(self, arr, k):
        arr.sort()
        n = len(arr)
        ans = 0
        i = n-1

        while i > 0:
            if arr[i]-arr[i-1]<k:
                ans+=arr[i]+arr[i-1]
                i-=2 # use both elements
            else:
                i-=1 # skip the larger element
        return ans