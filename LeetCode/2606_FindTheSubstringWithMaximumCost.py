from typing import List
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        char_to_val = {c:v for c,v in zip(chars, vals)}
        max_cost = 0
        curr_sum = 0
        min_prefix_sum = 0

        for char in s:
            char_val = char_to_val.get(char, ord(char)-ord('a')+1)
            curr_sum+=char_val
            max_cost = max(max_cost, curr_sum-min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, curr_sum)
        return max_cost