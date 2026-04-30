class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled_s = s+s
        # search for the original string starting from index 1(skip the first char), this avoids finding the string at position 0
        first_occurence_after_start = doubled_s.index(s,1)

        # if the string appears before reaching the end, it means the original string contains a repeated pattern
        return first_occurence_after_start<len(s)