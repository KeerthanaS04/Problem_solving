from math import ceil

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a, len_b = len(a), len(b)
        min_repetition = ceil(len_b/len_a)
        repeated_string_list = [a]*min_repetition

        # try upto 3 additional repetitions
        for _ in range(3):
            repeated_string = ''.join(repeated_string_list)
            if b in repeated_string:
                return min_repetition
            
            # if not found, add one more repetition
            min_repetition+=1
            repeated_string_list.append(a)
        return -1