class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)

        return sum(
            (i+1)*(n-i)
            for i, ch in enumerate(word)
            if ch in 'aeiou'
        )