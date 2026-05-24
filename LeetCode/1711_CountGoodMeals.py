from typing import List
from collections import Counter
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9+7
        max_sum = max(deliciousness)*2
        count_map = Counter()
        res = 0

        for curr_val in deliciousness:
            power_of_two=1
            while power_of_two<=max_sum:
                # find complement that would sum to power of two
                complement = power_of_two-curr_val

                # add count of complements seen so far
                res = (res+count_map[complement])%MOD
                power_of_two<<=1
            count_map[curr_val]+=1
        return res