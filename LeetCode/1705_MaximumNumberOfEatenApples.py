from typing import List
from heapq import heappush, heappop
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(days)
        curr_day = 0
        eaten = 0
        heap = []

        while curr_day < n or heap:
            if curr_day<n and apples[curr_day]>0:
                expire_day = curr_day + days[curr_day] - 1
                heappush(heap, (expire_day, apples[curr_day]))
            
            # remove all expired apples from the heap
            while heap and heap[0][0]<curr_day:
                heappop(heap)
            
            # eat one apple if available
            if heap:
                expire_day, apple_count = heappop(heap)
                apple_count -= 1
                eaten += 1
                
                if apple_count>0:
                    heappush(heap, (expire_day, apple_count))
            curr_day += 1
        return eaten