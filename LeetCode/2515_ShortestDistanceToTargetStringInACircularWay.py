from typing import List
class Solution:
    def closestTarget(self, words: List[int], target: str, startIndex: int) -> int:
        n = len(words)
        min_distance = n # Initialize with maximum possible distance

        for i, word in enumerate(word):
            if word==target:
                direct_idx = abs(i-startIndex)
                wrap_idx = n-direct_idx

                min_distance = min(min_distance, direct_idx, wrap_idx)
        return -1 if min_distance==n else min_distance