from typing import List
from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def top_two_freq(start_idx: int) -> tuple[int, int, int, int]:
            most_freq = 0
            sec_freq = 0

            freq_map = Counter(nums[start_idx::2])

            for val, count in freq_map.items():
                if freq_map[most_freq]<count:
                    sec_freq = most_freq
                    most_freq = val
                elif freq_map[sec_freq]<count:
                    sec_freq = val
            return (most_freq, sec_freq, freq_map[most_freq], freq_map[sec_freq])

        even_stats = top_two_freq(0)
        odd_stats = top_two_freq(1)

        n = len(nums)

        if even_stats[0]!=odd_stats[0]:
            # keep the most freq values at both positions
            return n-(even_stats[1]+odd_stats[1])
        return n-max(even_stats[1]+odd_stats[3], odd_stats[1]+even_stats[3])