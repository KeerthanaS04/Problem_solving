from typing import List
class Solution:
    def transformXOR(self, a: List[int], invert: bool=False) -> None:
        n = len(a)
        step = 1

        while step<n:
            for i in range(0, n, step*2):
                for j in range(i, i+step):
                    u = a[j]
                    v = a[j+step]
                    a[j] = u+v
                    a[j+step] = u-v
            step<<=1

        if invert:
            for i in range(n):
                a[i]//=n

    def xorConvolution(self, f: List[int], g: List[int]) -> List[int]:
        F = f[:]
        G = g[:]

        self.transformXOR(F)
        self.transformXOR(G)

        for i in range(len(F)):
            F[i]*=G[i]

        self.transformXOR(F, True)
        return F

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # remove duplicates
        values = set(nums)
        # smallest power of 2 greater than max element
        limit = 1
        while limit<=max(values):
            limit<<=1

        F = [0]*limit
        for x in values:
            F[x] = 1

        # pair XORs
        pair = self.xorConvolution(F, F)
        # triple XORs
        triple = self.xorConvolution(pair, F)
        ans = len(values)

        for x in range(limit):
            if x not in values and triple[x]>0:
                ans+=1
        return ans