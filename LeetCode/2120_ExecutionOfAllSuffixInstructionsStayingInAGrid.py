from typing import List
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
        m = len(s)
        directions = {
            'L': [0, -1],
            'R': [0, 1],
            'U': [-1, 0],
            'D': [1, 0]
        }

        for start_idx in range(m):
            curr_row, curr_col = startPos
            ans = 0
            for i in range(start_idx, m):
                row_delta, col_delta = directions[s[i]]
                next_row = curr_row+row_delta
                next_col = curr_col+col_delta

                if 0<=next_row<m and 0<=next_col<n:
                    curr_row = next_row
                    curr_col = next_col
                    ans+=1
                else:
                    break
            result.append(ans)
        return result