class Solution:
    def minMem(self, arr):
        n = len(arr)
        temp = [-1]*n

        for i in range(n):
            if arr[i]!=-1:
                idx = max(0, i-arr[i])
                temp[idx] = max(temp[idx], i+arr[i])

        ans = 0
        curr = -1
        mx = -1
        i = 0

        while i<n:
            mx = max(mx, temp[i])
            if curr<i:
                if mx<i:
                    return -1
                else:
                    curr = mx
                    ans+=1
            i+=1
        return ans