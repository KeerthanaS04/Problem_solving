from typing import List
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half_length = (intLength)>>1
        min_half = 10**(half_length-1)
        max_half = 10**half_length - 1

        res = []
        for query in queries:
            first_half_val = min_half+query-1
            if first_half_val>max_half:
                res.append(-1)
                continue

            first_half_str = str(first_half_val)
            palindrome_str = first_half_str+first_half_str[::-1][intLength%2:]
            res.append(int(palindrome_str))
        return res