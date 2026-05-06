class Solution:
    def sumXOR(self, arr):
        n = len(arr)
        total = 0

        # iterate over all 32 bits
        for i in range(32):
            oneCount = 0
            zeroCount = 0

            for num in arr:
                if (num>>i)&1:
                    oneCount += 1
                else:
                    zeroCount += 1
            
            total += oneCount * zeroCount * (1 << i)
        return total