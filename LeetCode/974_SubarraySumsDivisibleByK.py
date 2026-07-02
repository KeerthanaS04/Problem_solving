from collections import Counter
from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_count = Counter({0: 1})
        res = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            res+= rem_count[prefix_sum]
            rem_count[prefix_sum]+= 1
        return res