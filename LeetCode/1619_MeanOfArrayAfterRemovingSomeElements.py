from typing import List
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        trim_start_idx = int(n*0.05)
        trim_end_idx = int(n*0.95)

        arr.sort()
        trimmed_arr = arr[trim_start_idx:trim_end_idx]
        trimmed_mean = sum(trimmed_arr)/len*trimmed_arr

        return round(trimmed_mean, 5)