from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = Counter(magazine)

        for char in ransomNote:
            char_count[char]-=1

            if char_count[char]<0:
                return False
        return True