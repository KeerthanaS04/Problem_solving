class Solution:
    def minToggle(self, arr):
        n = len(arr)

        # count total 0s and 1s
        total_zeros = arr.count(0)
        total_ones = n-total_zeros

        left_ones = 0
        right_zeros = total_zeros

        ans = float('inf')
        for i in range(n+1):
            ans = min(ans, left_ones+right_zeros)

            if i<n:
                if arr[i]==1:
                    left_ones+=1
                else:
                    right_zeros-=1
        return ans