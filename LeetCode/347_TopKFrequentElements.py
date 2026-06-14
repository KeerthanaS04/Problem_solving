from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = Counter(nums)
        most_frequent_elements = freq_counter.most_common(k)
        res = [ele for ele, count in most_frequent_elements]
        return res