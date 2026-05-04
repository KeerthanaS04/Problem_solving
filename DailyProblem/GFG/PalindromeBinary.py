class Solution:
    def isBinaryPalindrome(self, n):
        binary = bin(n)[2:]  # Convert to binary and remove the '0b' prefix
        return binary==binary[::-1]