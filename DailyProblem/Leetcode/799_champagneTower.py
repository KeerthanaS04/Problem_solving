class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Create a 2D dp array
        tower = [[0.0]*101 for _ in range(101)]

        # Pour the champagne in the top one
        tower[0][0] = float(poured)

        # Fill the dp array
        for i in range(query_row+1):
            for j in range(i+1):
                if tower[i][j]>1.0:
                    overflow = tower[i][j] - 1.0

                    # keep only 1.0 in the current glass
                    tower[i][j] = 1.0

                    tower[i+1][j]+=overflow/2.0
                    tower[i+1][j+1]+=overflow/2.0
        
        # the max will be 1.0
        return min(1.0, tower[query_row][query_glass])