from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for string in strs:
            sorted_string = ''.join(sorted(string))
            anagram_groups[sorted_string].append(string)
        return list(anagram_groups.values())