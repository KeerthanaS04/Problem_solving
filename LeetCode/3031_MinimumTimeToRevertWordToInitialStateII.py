class Hashing:
    __slots__ = ['mod', 'h', 'p']

    def __init(self, s: str, base: int, mod: int) -> None:
        self.mod = mod
        # h[i] stores the hash value of prefix s[0:i]
        self.h = [0]*(len(s)+1)
        # p[i] stores base^i mod mod
        self.p = [1]*(len(s)+1)

        # build prefix hash and power arrays
        for i in range(1, len(s)+1):
            self.h[i] = (self.h[i-1]*base+ord(s[i-1]))%mod
            self.p[i] = (self.p[i-1]*base)%mod
    
    def query(self, l: int, r: int) -> int:
        return (self.h[r]-self.h[l-1]*self.p[r-l+1])%self.mod

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        hashing = Hashing(word, base=13331, mod=998244353)
        n = len(word)

        for i in range(k, n, k):
            if hashing .query(1, n-i)==hashing.query(i+1, n):
                return i//k
        return (n+k-1)//k