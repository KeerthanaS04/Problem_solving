from functools import reduce
from operator import xor
from typing import List
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9+7
        for l, r, k, v in queries:
            for idx in range(l, r+1, k):
                nums[idx] = nums[idx]*v%MOD
        return reduce(xor, nums)