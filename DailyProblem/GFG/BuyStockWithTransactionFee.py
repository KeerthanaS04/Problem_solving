class Solution:
    def maxProfit(self, arr, k):
        n = len(arr)
        pbs = -arr[0] # previous buy state
        pss = 0 # previous sell state

        for i in range(1, n):
            tbs = max(pbs, pss-arr[i])
            tss = max(pss, pbs+arr[i]-k)

            pbs = tbs
            pss = tss
        return pss