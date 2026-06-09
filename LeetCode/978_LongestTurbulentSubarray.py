from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)<=1:
            return len(arr)
        
        max_length = 1
        up_down = 1
        down_up = 1
        for i in range(1, len(arr)):
            prev_val = arr[i-1]
            curr_val = arr[i]

            if prev_val<curr_val:
                new_up_down = 1+down_up
                new_down_up = 1
            elif prev_val>curr_val:
                new_up_down = 1
                new_down_up = 1+up_down
            else:
                new_up_down = 1
                new_down_up = 1
            
            up_down = new_up_down
            down_up = new_down_up
            max_length = max(max_length, up_down, down_up)
        return max_length