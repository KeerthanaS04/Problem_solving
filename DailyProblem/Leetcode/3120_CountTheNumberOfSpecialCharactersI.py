from string import ascii_lowercase, ascii_uppercase
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_set = set(word)
        special_count = sum(
            lower_char in char_set and upper_char in char_set for lower_char, upper_char in zip(ascii_lowercase, ascii_uppercase)
        )
        return special_count