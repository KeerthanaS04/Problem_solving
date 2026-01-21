from typing import List
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            if num==2:
                result.append(-1)
            else:
                for bit in range(1, 32):
                    # Find the rightmost 0 bit
                    if (num>>bit)&1==0:
                        #flip the bit at position bit-1 to get the answer
                        result.append(num^(1<<(bit-1)))
                        break
        return result