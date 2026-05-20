from typing import List
from collections import Counter
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        freq_a = Counter()
        freq_b = Counter()

        for ele_a, ele_b in zip(A, B):
            freq_a[ele_a]+=1
            freq_b[ele_b]+=1

            common_count = sum(
                min(freq_in_a, freq_b[ele]) for ele, freq_in_a in freq_a.items()
            )
            res.append(common_count)
        return res