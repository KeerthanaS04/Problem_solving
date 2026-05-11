from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_to_idx = {word: i for i, word in enumerate(words)}
        res = []
        for curr_idx, curr_word in enumerate(words):
            for split_pos in range(len(curr_word)+1):
                prefix, suffix = curr_word[:split_pos], curr_word[split_pos:]
                reversed_prefix, reversed_suffix = prefix[::-1], suffix[::-1]

                # case 1: if reversed prefix exists and suffix is palindrome
                if reversed_prefix in word_to_idx and word_to_idx[reversed_prefix] != curr_idx and suffix==reversed_suffix:
                    res.append([curr_idx, word_to_idx[reversed_prefix]])
                
                # case 2: if reversed suffix exists and prefix is palindrome
                if split_pos>0 and reversed_suffix in word_to_idx and word_to_idx[reversed_suffix] != curr_idx and prefix==reversed_prefix:
                    res.append([word_to_idx[reversed_suffix], curr_idx])
        return res