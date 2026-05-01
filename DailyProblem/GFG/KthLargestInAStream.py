import heapq
class Solution:
    def kthLargest(self, arr, k):
        res = []
        min_heap = []

        for num in arr:
            heapq.heappush(min_heap, num)

            if len(min_heap)>k:
                heapq.heappop(min_heap)
            if len(min_heap)<k:
                res.append(-1)
            else:
                res.append(min_heap[0]) # smallest in heap = kth largest
        return res