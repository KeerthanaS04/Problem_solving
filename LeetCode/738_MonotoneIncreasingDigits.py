class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)

        i = 1 # breakdown point
        while i<length and digits[i-1]<=digits[i]:
            i+=1

        # If we found the breakdown point
        if i<length:
            while i>0 and digits[i-1]>digits[i]:
                digits[i-1] = str(int(digits[i-1])-1)
                i-=1
            
            while i<length:
                digits[i] = '9'
                i+=1
        return int(''.join(digits))