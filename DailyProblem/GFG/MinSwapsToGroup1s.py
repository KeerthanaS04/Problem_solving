class Solution:
    def minSwaps(self, arr):
        n = len(arr)
        count1 = sum(arr)
        if count1==0:
            return -1
        x = count1
        currOnes = 0
        maxOnes = 0

        for i in range(n):
            currOnes+=arr[i]

            if i>=x:
                currOnes-=arr[i-x]
            if i>=x-1:
                maxOnes = max(maxOnes, currOnes)
        return x-maxOnes