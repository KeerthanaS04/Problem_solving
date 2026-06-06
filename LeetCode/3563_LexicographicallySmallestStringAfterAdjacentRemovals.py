from string import ascii_lowercase
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        table = {ch: idx for idx, ch in enumerate(ascii_lowercase)}
        n = len(s)

        # positions of each character in the string
        pos = [[] for _ in range(26)]
        for idx, ch in enumerate(s):
            pos[table[ch]].append(idx)
        
        # bits[i]: bit j is set if index j can be reached from i
        # i.e, s[i] can be eventually removed together with s[j]
        bits = [0]*(n+1)

        for i in range(n-1, -1, -1):
            c = table[s[i]]
            mask = 0

            # consecutive characters in circular alphabet
            for d in ((c+1)%26, (c-1)%26):
                for k in pos[d]:
                    if k<=i:
                        continue

                    # k==i directly adjacent
                    # otherwise the substring b/w them must disappear completely
                    if k==i+1 or ((bits[i+1]>>(k-1))&1):
                        mask|=(1<<k)|bits[k+1]
            bits[i] = mask
        
        # dp[i] = lexicographically smallest string that can be obtained from s[i:]
        dp = [""]*(n+1)
        for i in range(n-1, -1, -1):
            # keep s[i]
            best = s[i]+dp[i+1]
            c = table[s[i]]

            # try removing s[i] together with s[k]
            for d in ((c+1)%26, (c-1)%26):
                for k in pos[d]:
                    if k<=i:
                        continue
                    if k==i+1 or ((bits[i+1]>>(k-1))&1):
                        candidate = dp[k+1]
                        if candidate<best:
                            best = candidate
            dp[i] = best
        return dp[0]