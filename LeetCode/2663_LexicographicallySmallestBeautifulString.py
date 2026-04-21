class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        char_list = list(s)

        for i in range(n-1, -1, -1):
            curr_char_val = ord(char_list[i])-ord('a')+1

            for next_val in range(curr_char_val, k):
                next_char = chr(ord('a')+next_val)

                # check if this char create a palindrome or not
                if i>0 and char_list[i-1]==next_char:
                    continue
                if i>1 and char_list[i-2]==next_char:
                    continue

                # valid char found
                char_list[i] = next_char

                # fill the remaining positions
                for pos in range(i+1, n):
                    for char_val in range(k):
                        candidate_char = chr(ord('a')+char_val)

                        if pos>0 and char_list[i-1]==candidate_char:
                            continue
                        if pos>1 and char_list[i-2]==candidate_char:
                            continue

                        # valid char found
                        char_list[pos] = candidate_char
                        break
                return ''.join(char_list)
        return ''