class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0
        for i, char in enumerate(s, 1):
            reverse_val = 26-(ord(char)-ord('a'))
            total_sum+=reverse_val*i
        return total_sum