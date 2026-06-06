from collections import deque
from functools import cache
from typing import List
class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        @cache
        def minmax(last_position: int, remaining_mask: int, is_alice_turn: int) -> int:
            # base case: if no pawns are left, return 0 moves needed
            if remaining_mask == 0:
                return 0
            if is_alice_turn:
                # maximize the total distance
                max_score = 0
                for pawn_idx, (pawn_x, pawn_y) in enumerate(positions):
                    # check if the pawn is still available (bit is set in remaining_mask)
                    if remaining_mask>>pawn_idx & 1:
                        # remove the pawn
                        new_mask = remaining_mask^(1<<pawn_idx)
                        score = minmax(pawn_idx, new_mask, is_alice_turn^1) + distances[last_position][pawn_x][pawn_y]
                        if score > max_score:
                            max_score = score
                return max_score
            else:
                # minimize the total distance
                min_score = float('inf')
                for pawn_idx, (pawn_x, pawn_y) in enumerate(positions):
                    if remaining_mask>>pawn_idx & 1:
                        new_mask = remaining_mask^(1<<pawn_idx)
                        score = minmax(pawn_idx, new_mask, is_alice_turn^1) + distances[last_position][pawn_x][pawn_y]
                        if score < min_score:
                            min_score = score
                return min_score

        #Initialize variables
        num_pawns = len(positions)
        board_size = 50

        # create 3D array to store distances from each position to all board cells
        distances = [[[-1]*board_size for _ in range(board_size)] for _ in range(num_pawns+1)]

        # knights possible moves (8 directions)
        knight_x = [2, 2, -2, -2, 1, 1, -1, -1]
        knight_y = [1, -1, 1, -1, 2, -2, 2, -2]

        # add knight's starting position as the last element in positions
        positions.append([kx, ky])

        # BFS to compute minimum distances from each position to all board cells
        for position_idx, (start_x, start_y) in enumerate(positions):
            distances[position_idx][start_x][start_y] = 0
            queue = deque([(start_x, start_y)])
            curr_distance = 0

            while queue:
                curr_distance += 1
                for _ in range(len(queue)):
                    curr_x, curr_y = queue.popleft()

                    # try all possible 8 moves
                    for move_idx in range(8):
                        next_x = curr_x + knight_x[move_idx]
                        next_y = curr_y + knight_y[move_idx]

                        # check if the move is within bounds and not visited
                        if 0 <= next_x < board_size and 0 <= next_y < board_size and distances[position_idx][next_x][next_y] == -1:
                            distances[position_idx][next_x][next_y] = curr_distance
                            queue.append((next_x, next_y))
        
        res = minmax(num_pawns, (1<<num_pawns)-1, 1)
        minmax.cache_clear()
        return res