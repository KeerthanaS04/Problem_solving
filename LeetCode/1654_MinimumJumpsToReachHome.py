from collections import deque
from typing import List
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_pos = set(forbidden)
        # Initialize bfs with starting position
        queue = deque([(0,1)]) # (curr_pos, last_jump_direction)
        visited = {(0,1)} # (pos, direction)
        jumps = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_pos, can_jump_back = queue.popleft()

                if curr_pos==x:
                    return jumps
                
                next_positions = [(curr_pos+a, 1)] # forward jump always allowed
                if can_jump_back&1:
                    next_positions.append((curr_pos-b, 0)) # backward jump only if last jump was not backward
                
                for next_pos, next_can_jump_back in next_positions:
                    if 0<=next_pos<=6000 and (next_pos, next_can_jump_back) not in visited and next_pos not in forbidden_pos:
                        visited.add((next_pos, next_can_jump_back))
                        queue.append((next_pos, next_can_jump_back))
            jumps += 1
        return -1