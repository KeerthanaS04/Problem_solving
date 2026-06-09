from itertools import permutations
from math import inf
from string import ascii_lowercase
class Solution:
    def largestVariance(self, s: str) -> int:
        max_variance = 0

        # try all possible pairs of distinct characters
        for char_high, char_low in permutations(ascii_lowercase, 2):
            if char_high==char_low:
                continue

            # dp[0]: max difference when we haven't seen char_low yet - counting of a continuous char
            # dp[1]: max difference when we have seen char_low - distance between char_low and char_high
            dp = [0, -inf]

            for curr_char in s:
                if curr_char==char_high:
                    dp[0]+=1
                    dp[1]+=1
                elif curr_char==char_low:
                    dp[1] - max(dp[1]-1, dp[0]-1) # if a new char comes, distance and count of continuous char decreases
                    dp[0] = 0 # if a new char comes, count of continuous char resets
                
                if max_variance<dp[1]:
                    max_variance = dp[1]
        return max_variance