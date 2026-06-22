class Solution:
    def chooseSwap(self, s):
        s = list(s)
        remaining = set(s)

        for i in range(len(s)):
            remaining.discard(s[i])

            for ch in sorted(remaining):
                if ch<s[i]:
                    x, y = s[i], ch

                    for j in range(len(s)):
                        if s[j]==x:
                            s[j] = y
                        elif s[j]==y:
                            s[j] = x
                    return ''.join(s)
        return ''.join(s)