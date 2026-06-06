class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook_row, rook_col = a, b
        bishop_row, bishop_col = c, d
        queen_row, queen_col = e, f

        # check if rook can capture the queen in 1 move
        # rook and queen are in the same row and bishop doesn't block the path (bishop is on the same side of rook_col and queen_col)
        if rook_row==queen_row and (bishop_row!=rook_row or (bishop_col-rook_col)*(bishop_col-queen_col)>0):
            return 1
        # rook and queen are in the same column and bishop doesn't block the path (bishop is on the same side of rook_row and queen_row)
        if rook_col==queen_col and (bishop_col!=rook_col or (bishop_row-rook_row)*(bishop_row-queen_row)>0):
            return 1
        
        # check if bishop can capture the queen in 1 move
        # bishop and queen are on the same diagonal and rook doesn't block the path (rook is not on the same diagonal or is on the same diagonal but on the opposite side of bishop and queen)
        if bishop_row-queen_row==bishop_col-queen_col and (rook_row-queen_row!=rook_col-queen_col or (rook_row-bishop_row)*(rook_row-queen_row)>0):
            return 1
        
        if bishop_row-queen_row==queen_col-bishop_col and (rook_row-queen_row!=queen_col-rook_col or (rook_row-bishop_row)*(rook_row-queen_row)>0):
            return 1
        return 2