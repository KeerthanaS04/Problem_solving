from typing import List
class Solution:
    def queensAttackTheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        BOARD_SIZE = 8
        # convert queen positions to tuple
        queen_positions = {(row, col) for row, col in queens}
        attacking_queens = []

        # check all directions: vertical, horizontal, diagonal
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr==0 and dc==0:
                    continue

                # start from king's position
                curr_row, curr_col = king

                # move in the current direction until we go out of bounds or find a queen
                while 0<=curr_row+dr<BOARD_SIZE and 0<=curr_col+dc<BOARD_SIZE:
                    curr_row += dr
                    curr_col += dc

                    if (curr_row, curr_col) in queen_positions:
                        attacking_queens.append([curr_row, curr_col])
                        break
        return attacking_queens