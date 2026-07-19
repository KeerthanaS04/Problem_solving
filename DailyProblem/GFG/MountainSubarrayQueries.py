class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)

        inc = [0]*n
        dec = [0]*n

        # build inc
        inc[n-1] = n-1
        for i in range(n-2, -1, -1):
            if arr[i]<=arr[i+1]:
                inc[i] = inc[i+1]
            else:
                inc[i] = i
        
        # build dec
        dec[0] = 0
        for i in range(1, n):
            if arr[i]<=arr[i-1]:
                dec[i] = dec[i-1]
            else:
                dec[i] = i
        
        ans = []
        for l, r in queries:
            ans.append(inc[l]>=dec[r])

        return ans