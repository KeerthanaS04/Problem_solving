#include<bits/stdc++.h>
using namespace std

class Solution {
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        // Create prefix sum arrays for rows and columns
        vector<vector<int>> rowSum(m + 1, vector<int>(n + 1));
        vector<vector<int>> colSum(m + 1, vector<int>(n + 1));

        // Fill prefix sum arrays
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                rowSum[i][j] = rowSum[i][j - 1] + grid[i - 1][j - 1];
                colSum[i][j] = colSum[i - 1][j] + grid[i - 1][j - 1];
            }
        }

        // Search for the largest magic square beginning from the largest possible size
        for (int k = min(m, n); k > 1; --k) {
            for (int i = 0; i + k - 1 < m; ++i) {
                for (int j = 0; j + k - 1 < n; ++j) {
                    int i2 = i + k - 1, j2 = j + k - 1;
                    // Check if the current square is a magic square
                    if (checkingMagicSquare(grid, rowSum, colSum, i, j, i2, j2))
                        return k; // Return size if it's a magic square
                }
            }
        }

        // If no larger magic square is found, return 1 as the default size
        return 1;
    }

    // Function to check if square is magic
    bool checkingMagicSquare(vector<vector<int>>& grid, vector<vector<int>>& rowSum, vector<vector<int>>& colSum, int topLeftX, int topLeftY, int bottomRightX, int bottomRightY){
        // The value that rows, columns, and diagonals should sum to
        int targetSum = rowSum[topLeftX + 1][bottomRightY + 1] - rowSum[topLeftX + 1][topLeftY];

        // Check sums of all rows
        for (int i = topLeftX + 1; i <= bottomRightX; ++i)
            if (rowSum[i + 1][bottomRightY + 1] - rowSum[i + 1][topLeftY] != targetSum)
                return false;

        // Check sums of all columns
        for (int j = topLeftY; j <= bottomRightY; ++j)
            if (colSum[bottomRightX + 1][j + 1] - colSum[topLeftX][j + 1] != targetSum)
                return false;

        // Check diagonal (top-left to bottom-right)
        int sumDiagonal = 0;
        for (int i = topLeftX, j = topLeftY; i <= bottomRightX; ++i, ++j)
            sumDiagonal += grid[i][j];
        if (sumDiagonal != targetSum)
            return false;

        // Check anti-diagonal (top-right to bottom-left)
        sumDiagonal = 0;
        for (int i = topLeftX, j = bottomRightY; i <= bottomRightX; ++i, --j)
            sumDiagonal += grid[i][j];
        if (sumDiagonal != targetSum)
            return false;

        // If all checks pass, it's a magic square
        return true;
    }
};