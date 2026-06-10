from typing import List
from itertools import pairwise
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        total_operations = 0
        distinct_count = 0

        for prev_val, curr_val in pairwise(nums):
            if prev_val!=curr_val:
                distinct_count+=1
            total_operations+=distinct_count
        return total_operations