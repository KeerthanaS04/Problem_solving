class Solution:
    def largestArea(self, n, m, arr):
        k = len(arr)
        if k==0:
            return n*m
        
        rows = [0]*k
        cols = [0]*k

        for i in range(k):
            rows[i] = arr[i][0]
            cols[i] = arr[i][1]
        
        rows.sort()
        cols.sort()

        # maximum consecutive rows available
        max_rows = rows[0] - 1
        for i in range(1, k):
            max_rows = max(max_rows, rows[i] - rows[i-1] - 1)
        max_rows = max(max_rows, n - rows[-1])

        # maximum consecutive columns available
        max_cols = cols[0] - 1
        for i in range(1, k):
            max_cols = max(max_cols, cols[i] - cols[i-1] - 1)
        max_cols = max(max_cols, m - cols[-1])
        
        return max_rows * max_cols