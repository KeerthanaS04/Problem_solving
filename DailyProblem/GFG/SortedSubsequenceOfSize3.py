class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n<3:
            return []
        small = [0]*n
        big = [0]*n

        # fill small
        small[0] = arr[0]
        for i in range(1, n):
            small[i] = min(arr[i], small[i-1])
        
        # fill big
        big[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            big[i] = max(arr[i], big[i+1])
        
        # find valid triplet
        for i in range(n):
            if arr[i]>small[i] and arr[i]<big[i]:
                return [small[i], arr[i], big[i]]
        return []