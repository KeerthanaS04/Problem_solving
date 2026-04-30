from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap)>1:
            first_stone = -heapq.heappop(max_heap)
            sec_stone = -heapq.heappop(max_heap)

            if first_stone!=sec_stone:
                heapq.heappush(max_heap, -(first_stone-sec_stone))
        return 0 if not max_heap else -max_heap[0]