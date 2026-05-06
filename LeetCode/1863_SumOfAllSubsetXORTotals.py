from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        # iterate through all possible subsets using bit representation. There are 2^n possible subsets for n elements
        for subset in range(1<<n):
            xor_val = 0

            # check each bit pos to determine which elements are in curr subset
            for bit_pos in range(n):
                if (subset>>bit_pos)&1: # if the bit at bit_pos is set, include nums[bit_pos] in the XOR calculation
                    xor_val ^= nums[bit_pos]
            total += xor_val
        return total