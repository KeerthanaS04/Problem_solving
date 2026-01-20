from typing import List
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            if num==2:
                result.append(-1)
            else:
                #Find the rightmost 0 bit
                for bit in range(1,32):
                    #check if current bit is 0
                    if ((num>>bit)&1)==0:
                        ans = num^(1<<(bit-1))
                        result.append(ans)
                        break
        return result