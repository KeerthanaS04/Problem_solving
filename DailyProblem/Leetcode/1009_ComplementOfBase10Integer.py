class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        
        result = 0
        bit_position = 0

        while n>0:
            #take the rightmost bit and flip it
            flipped_bit = (n&1)^1
            result+=flipped_bit<<bit_position
            bit_position+=1
            n>>=1
        return result