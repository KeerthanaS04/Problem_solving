from itertools import count

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for candidate in count(n):
            digit_prod = 1
            temp_num = candidate

            while temp_num > 0:
                digit = temp_num % 10
                digit_prod *= digit
                temp_num //= 10
            if digit_prod % t == 0:
                return candidate