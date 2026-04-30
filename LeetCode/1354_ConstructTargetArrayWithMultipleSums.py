from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total_sum = sum(target)
        max_heap = [-num for num in target]
        heapify(max_heap)

        while -max_heap[0]>1:
            curr_max = -heappop(max_heap)
            sum_remain = total_sum-curr_max

            if sum_remain==0 or curr_max-sum_remain<1:
                return False
            
            prev_val = (curr_max%sum_remain) or sum_remain
            heappush(max_heap, -prev_val)

            total_sum = total_sum-curr_max+prev_val
        return True