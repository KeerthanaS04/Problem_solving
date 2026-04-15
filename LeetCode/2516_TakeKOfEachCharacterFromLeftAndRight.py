from typing import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        char_cnt = Counter(s)

        if any(char_cnt[char]<k for char in 'abc'):
            return -1
        
        max_window_size = 0
        left = 0
        for right, char in enumerate(s):
            char_cnt[char]-=1
            while char_cnt[char]<k:
                char_cnt[left]+=1
                left+=1
            max_window_size = max(max_window_size, right-left+1)
        return len(s)-max_window_size