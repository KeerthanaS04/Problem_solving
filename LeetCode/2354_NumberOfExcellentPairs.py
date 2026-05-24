from typing import List
from collections import Counter
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        unique_nums = set(nums)
        count = 0

        # count the frequency of each bit count value
        bit_count_freq = Counter()
        for num in unique_nums:
            bit_count_freq[num.bit_count()]+=1
        for num in unique_nums:
            curr_bit_count = num.bit_count()

            # check all possible bit counts and add valid pairs
            for other_bit_count, freq in bit_count_freq.items():
                # a pair is excellent if sum of bits count>=k
                if curr_bit_count+other_bit_count>=k:
                    count+=1
        return count