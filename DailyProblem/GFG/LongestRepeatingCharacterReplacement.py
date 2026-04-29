from collections import Counter
class Solution:
    def longestSubstr(self, s, k):
        char_count = Counter()
        l = 0
        max_freq = 0

        for r, char in enumerate(s):
            char_count[char]+=1
            max_freq = max(max_freq, char_count[char])

            # invalid if window_size-max_freq>k
            if r-l+1-max_freq>k:
                char_count[s[l]]-=1
                l+=1
        return len(s)-l