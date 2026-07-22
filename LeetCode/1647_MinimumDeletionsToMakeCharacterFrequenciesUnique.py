from typing import List
from collections import Counter
from math import inf
class Solution:
    def minDeletions(self, s: str) -> int:
        char_freq = Counter(s)
        deletions = 0
        prev_freq = inf

        for curr_freq in sorted(char_freq.values(), reverse=True):
            # if prev_freq is 0, we must delete all occurences of curr char
            if prev_freq == 0:
                deletions+=curr_freq
            elif curr_freq>=prev_freq:
                # delete enough chars, to make freq = prev-1
                deletions+=(curr_freq-prev_freq+1)
                prev_freq-=1
            else:
                prev_freq=curr_freq
        return deletions