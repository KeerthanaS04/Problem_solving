from typing import List
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        curr_idx = 0
        max_captured = 0

        while curr_idx<n:
            next_idx = curr_idx+1

            if forts[curr_idx]!=0:
                while next_idx<n and forts[next_idx]==0:
                    next_idx+=1
                
                if next_idx<n and forts[curr_idx]+forts[next_idx]==0:
                    # number of empty positions between the two ports
                    captured_count = next_idx-curr_idx-1
                    max_captured = max(max_captured, captured_count)
            curr_idx = next_idx
        return max_captured