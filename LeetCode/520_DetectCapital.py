class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uppercase_count = sum(1 for char in word if char.isupper())

        return (uppercase_count==0 or uppercase_count==len(word) or (uppercase_count==1 and word[0].isupper()))