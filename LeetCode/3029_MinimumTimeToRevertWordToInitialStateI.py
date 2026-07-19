class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        for i in range(k, n, k):
            if word[i:]==word[:n-i]:
                return i//k
        return (n+k-1)//k