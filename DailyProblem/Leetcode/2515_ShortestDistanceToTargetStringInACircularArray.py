from typing import List
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        short_dist = n # Initialize with max possibel distance

        for i, word in enumerate(words):
            if word==target:
                direct_dist = abs(i-startIndex)
                wrap_dist = n-direct_dist
                short_dist = min(short_dist, direct_dist, wrap_dist)
        return -1 if short_dist==n else short_dist