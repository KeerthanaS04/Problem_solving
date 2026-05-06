class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_possible_k = len(sequence)//len(word)

        # start from the largest possible value for optimization
        for k in range(max_possible_k, -1, -1):
            if word*k in sequence:
                return k
        return 0