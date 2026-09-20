class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}
        for char in t:
            char_count[char]-= 1
            if char_count[char]<0:
                return False
        return True