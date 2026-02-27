class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = False

        # we will go from rightmost to left except the leftmost bit, because we need to go till 1
        for bit in s[:0:-1]:
            if carry:
                if bit=='0':
                    bit = '1'
                    carry=False
                else:
                    bit='0'
            
            if bit=='1': # if current bit is 1, add 1
                steps+=1
                carry=True
            steps+=1 # divide by 2
        
        if carry:
            steps+=1
        return steps