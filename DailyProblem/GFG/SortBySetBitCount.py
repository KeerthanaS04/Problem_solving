class Solution:
    def sortBySetBitCount(self, arr):
        n = len(arr)

        # Initialize 32 buckets
        buckets = [[] for _ in range(32)]
        for num in arr:
            count = self.setBitCount(num)
            buckets[count].append(num)
        
        # rebuild res fron high set bits to low
        res = []
        for i in range(31, -1, -1):
            res.extend(buckets[i])
        return res
    
    def setBitCount(self, n):
        count = 0
        while n>0:
            if n&1==1:
                count+=1
            n = n>>1    
        return count