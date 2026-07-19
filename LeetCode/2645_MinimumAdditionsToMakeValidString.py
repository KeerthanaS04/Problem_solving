class Solution:
    def addMinimum(self, word: str) -> int:
        pattern = 'abc'
        additions_needed = 0
        n = len(word)

        word_idx = 0
        pattern_idx = 0

        while word_idx<n:
            if word[word_idx]!=pattern[pattern_idx]:
                additions_needed += 1
            else:
                word_idx += 1
            pattern_idx = (pattern_idx+1)%3
        
        # handle incomplete pattern
        if word[-1]!='c':
            if word[-1]=='b':
                additions_needed += 1
            else:
                additions_needed += 2
        return additions_needed