from math import gcd
from typing import List
class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        group_size = gcd(n,k)
        total = 0

        for group_start in range(group_size):
            group_elements = sorted(arr[group_start:n:group_size])
            median_idx = len(group_elements)>>1
            median_val = group_elements[median_idx]
            total += sum(abs(median_val - num) for num in group_elements)
        return total