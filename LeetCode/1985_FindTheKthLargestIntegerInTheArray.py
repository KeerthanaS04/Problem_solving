from typing import List
from heapq import nlargest
class Solution:
    def findKthLargest(self, nums: List[str], k: int) -> int:
        # use heapq.nlargest to get the k largest elements
        k_largest_numbers = nlargest(k, nums, key=lambda x: int(x))
        return k_largest_numbers[k-1]