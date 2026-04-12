class Solution:
    def minTimeToType(self, word: str) -> int:
        total_time = len(word)
        curr_pos = ord('a')

        for char in word:
            char_pos = ord(char)
            direct_dist = abs(curr_pos - char_pos)
            wrap_dist = 26-direct_dist
            total_time+=min(direct_dist, wrap_dist)
            curr_pos = char_pos
        return total_time