from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = (0,1,0,-1,0)
        obstacle = {(x,y) for x,y in obstacles}
        max_sq_dist = 0
        dir_index = 0
        curr_x, curr_y = 0, 0

        for command in commands:
            if command==-2:
                dir_index = (dir_index+3)%4
            elif command==-1:
                dir_index = (dir_index+1)%4
            else:
                # move forward
                for _ in range(command):
                    next_x = curr_x+directions[dir_index]
                    next_y = curr_y+directions[dir_index+1]

                    if (next_x, next_y) in obstacle:
                        break

                    curr_x, curr_y = next_x, next_y
                    max_sq_dist = max(max_sq_dist, curr_x**2+curr_y**2)
        return max_sq_dist