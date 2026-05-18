from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a','e','i','o','u'}
        vowel_to_indices = []

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                vowel_to_indices.append(i)
        
        # process each query to count vowel strings in the given range
        res = []
        for l,r in queries:
            count = bisect_right(vowel_to_indices,r)-bisect_left(vowel_to_indices, l)
            res.append(count)
        return res