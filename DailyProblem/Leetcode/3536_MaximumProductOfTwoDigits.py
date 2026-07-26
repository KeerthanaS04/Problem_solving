class Solution:
    def maxProduct(self, n: int) -> int:
        largest = 0
        sec_largest = 0

        while n > 0:
            n, curr_digit = divmod(n, 10)

            if curr_digit > largest:
                sec_largest = largest
                largest = curr_digit
            elif curr_digit > sec_largest:
                sec_largest = curr_digit
        return largest * sec_largest