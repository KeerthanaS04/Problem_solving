class Solution:
    def areIsomorphic(self, s1, s2):
        s1_to_s2 = {}
        s2_to_s1 = {}

        for char_s1, char_s2 in zip(s1, s2):
            if char_s1 in s1_to_s2 and s1_to_s2[char_s1]!=char_s2:
                return False
            if char_s2 in s2_to_s1 and s2_to_s1[char_s2]!=char_s1:
                return False
            
            s1_to_s2[char_s1] = char_s2
            s2_to_s1[char_s2] = char_s1

        return True