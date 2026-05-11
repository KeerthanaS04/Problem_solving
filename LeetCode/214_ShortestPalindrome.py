class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # prime base for polynomial rolling hash
        BASE = 131
        MOD = 10**9 + 7
        n = len(s)
        prefix_hash, suffix_hash = 0, 0
        base_power = 1
        longest_palindrome_end = 0

        for i, char in enumerate(s):
            char_val = ord(char) - ord('a') + 1
            # hash = hash * BASE + char_val
            prefix_hash = (prefix_hash * BASE + char_val) % MOD
            # hash = char_val * base_power + hash
            suffix_hash = (char_val * base_power + suffix_hash) % MOD
            base_power = (base_power * BASE) % MOD

            if prefix_hash == suffix_hash:
                longest_palindrome_end = i + 1
        if longest_palindrome_end == n:
            return s
        non_palindrome_suffix = s[longest_palindrome_end:]
        return non_palindrome_suffix[::-1] + s