from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = Counter(words)
        res = 0
        odd_palindrome = 0

        for word, freq in word_count.items():
            if word[0] == word[1]: # if the word is a palindrome
                # word is a palindrome itself
                odd_palindrome += freq&1
                # Add pairs of palindromic words (each pair contributes 4 to the length)
                res += (freq//2)*4
            else: # if the word is not a palindrome
                res+=min(freq, word_count[word[::-1]])*2
        res+=2 if odd_palindrome>0 else 0 # add one odd palindrome in the middle if exists
        return res