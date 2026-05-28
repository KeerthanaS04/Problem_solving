from string import ascii_lowercase, ascii_uppercase

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_occurence = {}
        last_occurence = {}

        for idx, char in enumerate(word):
            if char not in first_occurence:
                first_occurence[char] = idx
            last_occurence[char] = idx
        
        special_count = sum(
            lower_char in last_occurence and upper_char in first_occurence and last_occurence[lower_char]<first_occurence[upper_char]
            for lower_char, upper_char in zip(ascii_lowercase, ascii_uppercase)
        )
        return special_count