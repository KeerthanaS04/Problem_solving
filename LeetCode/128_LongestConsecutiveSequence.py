from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        remaining_nums = set(nums)
        max_length = 0
        sequence_length = {}

        for curr_num in nums:
            if curr_num not in remaining_nums:
                continue
            sequence_end = curr_num
            while sequence_end in remaining_nums:
                remaining_nums.remove(sequence_end)
                sequence_end+=1
            # if sequence end is already there we can use its cached length
            curr_length = sequence_end-curr_num+sequence_length.get(sequence_end, 0)
            sequence_length[curr_num] = curr_length
            max_length = max(max_length, curr_length)
        return max_length