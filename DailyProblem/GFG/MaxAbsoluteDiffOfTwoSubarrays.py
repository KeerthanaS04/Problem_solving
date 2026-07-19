class Solution:
    def maxDiffSubarrays(self, arr):
        n = len(arr)
        INF = 10**9

        left_max = [0]*n
        left_min = [0]*n

        # maximum subarray sum in prefix [0...i]
        curr = arr[0]
        left_max[0] = arr[0]
        for i in range(1, n):
            curr = max(arr[i], curr+arr[i])
            left_max[i] = max(left_max[i-1], curr)

        # minimum subarray sum in prefix [0...i]
        curr = arr[0]
        left_min[0] = arr[0]
        for i in range(1, n):
            curr = min(arr[i], curr+arr[i])
            left_min[i] = min(left_min[i-1], curr)
        
        right_max = [0]*n
        right_min = [0]*n

        # maximum subarray sum in suffix [i...n-1]
        curr = arr[-1]
        right_max[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            curr = max(arr[i], curr+arr[i])
            right_max[i] = max(right_max[i+1], curr)

        # minimum subarray sum in suffix [i...n-1]
        curr = arr[-1]
        right_min[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            curr = min(arr[i], curr+arr[i])
            right_min[i] = min(right_min[i+1], curr)
        
        ans = -INF
        for i in range(n-1):
            case1 = abs(right_max[i+1]-left_min[i])
            case2 = abs(left_max[i]-right_min[i+1])
            ans = max(ans, case1, case2)
        return ans