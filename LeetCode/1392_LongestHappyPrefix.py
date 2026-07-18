class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in range(1, len(s)):
            if s[:-i]==s[i:]:
                return s[i:]
        # no common prefix/suffix found
        return ''