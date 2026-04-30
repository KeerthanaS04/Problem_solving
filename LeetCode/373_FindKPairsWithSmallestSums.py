from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = [[num1+nums2[0], i, 0] for i, num1 in enumerate(nums1[:k])]
        heapify(min_heap)
        res = []

        while min_heap and k>0:
            _, index1, index2 = heappop(min_heap)
            res.append([nums1[index1], nums2[index2]])
            k-=1

            if index2+1<len(nums2):
                new_sum = nums1[index1]+nums2[index2+1]
                heappush(min_heap, [new_sum, index1, index2+1])
        return res