from collections import Counter
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hash map to store prefix sum frequencies
        prefix_sum_count = Counter({0:1})
        result = 0
        curr_sum = 0

        for num in nums:
            curr_sum+=num

            # if (curr_sum-k) exists, it means there are subarrays ending at current index whose sum equals k
            result+=prefix_sum_count[curr_sum-k]
            prefix_sum_count[curr_sum]+=1
        return result