from typing import List
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total_sum = sum(beans)
        n = len(beans)

        min_removals = min(total_sum-bean_count*(n-i) for i, bean_count in enumerate(beans))
        return min_removals