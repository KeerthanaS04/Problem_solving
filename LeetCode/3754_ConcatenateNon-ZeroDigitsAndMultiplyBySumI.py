class Solution:
    def sumAnMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0

        for ch in str(n):
            if ch != '0':
                digit = int(ch)
                x = x * 10 + digit
                digit_sum += digit
        
        return x * digit_sum