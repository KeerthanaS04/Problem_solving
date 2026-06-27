from collections import Counter
from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        # special case for 1
        max_length = freq_map[1]-(freq_map[1]%2^1)
        del freq_map[1]

        for num in freq_map:
            curr_length = 0
            curr_num = num

            while freq_map[curr_num]>1:
                curr_num = curr_num*curr_num
                curr_length+=2
            
            # if the final squared num exists, add it as a center element, otherwise subtract 1 from the length
            if freq_map[curr_num]:
                curr_length+=1
            else:
                curr_length-=1

            max_length = max(max_length, curr_length)

        return max_length