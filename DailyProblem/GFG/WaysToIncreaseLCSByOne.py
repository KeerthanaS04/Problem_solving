class Solution:
    def waysToIncreaseLCSBy1(self, s1, s2):
        n = len(s1)
        m = len(s2)

        # prefix
        pref = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    pref[i][j] = pref[i - 1][j - 1] + 1
                else:
                    pref[i][j] = max(pref[i - 1][j], pref[i][j - 1])
        
        # suffix
        suff = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    suff[i][j] = suff[i + 1][j + 1] + 1
                else:
                    suff[i][j] = max(suff[i + 1][j], suff[i][j + 1])
        
        lcs = pref[n][m]
        ans = 0

        # try every insertion position
        for pos in range(n+1):
            visited = set()
            for j in range(m):
                c = s2[j]

                # avoid containing same character twice at same position
                if c in visited:
                    continue
                if pref[pos][j]+1+suff[pos][j+1] == lcs+1:
                    ans += 1
                    visited.add(c)
        return ans