class Solution:
    def findMaxProduct(self, arr):
        MOD = 10**9 + 7
        if len(arr) == 1:
            return arr[0]
        
        neg_count = 0
        zero_count = 0
        product = 1
        max_neg = -float('inf')

        for x in arr:
            if x==0:
                zero_count += 1
                continue
            if x < 0:
                neg_count += 1
                max_neg = max(max_neg, x)
            product*= x
        if zero_count == len(arr):
            return 0
        if neg_count==1 and zero_count+neg_count == len(arr):
            return 0
        if neg_count % 2 == 1:
            product //= max_neg
        return product % MOD