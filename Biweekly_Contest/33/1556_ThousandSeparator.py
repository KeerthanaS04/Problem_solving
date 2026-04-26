class Solution:
    def thousandSeparator(self, n: int) -> str:
        digit_count = 0
        res = []

        while True:
            n, digit = divmod(n, 10)
            res.append(str(digit))
            digit_count+=1

            if n==0:
                break

            if digit_count==3:
                res.append('.')
                digit_count=0
        return ''.join(res[::-1])