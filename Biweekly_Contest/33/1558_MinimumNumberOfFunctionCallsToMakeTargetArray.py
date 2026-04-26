from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # count total number of set bits (1s) in binary representation of all numbers
        total_set_bits = sum(nums.bit_count() for num in nums)
        # find the highest bit position among all numbers
        max_bit_pos = max(0, max(nums).bit_length()-1) if nums else 0

        return total_set_bits+max_bit_pos