from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        char_count = Counter(s)
        target_count = Counter(target)

        return min(char_count[c]//target_count[c] for c in target_count)