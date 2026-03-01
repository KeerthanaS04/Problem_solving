class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        nonzeroIndex = 0

        for i in range(n):
            if arr[i]!=0:
                arr[nonzeroIndex], arr[i] = arr[i], arr[nonzeroIndex]
                nonzeroIndex+=1