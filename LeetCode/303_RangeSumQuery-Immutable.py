from itertools import accumulate
from typing import List
class NumArray:
    def __init(self, nums: List[List[int]]):
        self.prefix_sum = list(accumulate(nums, initial=0))
    
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]