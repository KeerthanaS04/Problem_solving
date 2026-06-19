class Solution:
    def optimalArray(self, arr):
        n = len(arr)
        prefix = [0]*(n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
        
        ans = [0]*n
        for i in range(n):
            mid = i//2
            median = arr[mid]
            left_cost = median*(mid+1)-prefix[mid+1]
            right_cost = (prefix[i+1]-prefix[mid+1])-median*(i-mid)

            ans[i] = left_cost+right_cost
        return ans