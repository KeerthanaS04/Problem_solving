import heapq
class Solution:
    def maxAmount(self, arr, k):
        MOD = 10**9 + 7

        # max heap
        heap = [-x for x in arr]
        heapq.heapify(heap)

        res = 0
        while k>0 and heap:
            x = -heapq.heappop(heap)
            res = (res + x) % MOD

            x-=1
            k-=1
            if k>0:
                heapq.heappush(heap, -x)
        return res