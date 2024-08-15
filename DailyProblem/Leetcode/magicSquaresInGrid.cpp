#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
        int numMagicSquaresInside(vector<vector<int>>& grid){
            int rows = grid.size(); //total number of rows in the grid
            int cols = grid[0].size(); //total number of columns in the grid
            int magicSquareCount = 0;

            // Lambda function to check if the 3x3 grid with top-left corner at (i,j) is a magicSquare
            auto isMagicSquare = [&](int i, int j) -> int{
                // Check if the square extends beyond the grid boundaries
                if(i + 3 > rows || j + 3 > cols){
                    return 0;
                }

                vector<int> count(16,0); // Count for numbers 1 to 9 within the 3x3 grid
                vector<int> sumRow(3,0); // Sum of each row within the 3x3 grid
                vector<int> sumCol(3, 0); //Sum of each Col within the 3x3 grid

                int diagSum1 = 0;  //Sum of the first diagonal
                int diagSum2 = 0;  //Sum of the second diagonal

                //Iterate over the 3x3 grid and populate sum and counts
                for(int x=i; x<i+3; x++){
                    for(int y=j; y<j+3; y++){
                        int value = grid[x][y];
                        // Check for invalid numbers or duplicates
                        if(value < 1 || value > 9 || ++count[value]>1) return 0;

                        // Update row and column sums
                        sumRow[x - i] += value;
                        sumCol[y - j] += value;

                        // Update diagonal sums
                        if(x-i == y-j){
                            diagSum1 += value;
                        }
                        if(x-i + y-j == 2){
                            diagSum2 += value;
                        }
                    }
                }
                // Check if both the diagonal sum have the same sum or not
                if(diagSum1 != diagSum2) return 0;
                // Check if each row and column sum to the same value as the diagonals
                for(int k=0; k<3; k++){
                    if(sumRow[k] != diagSum1 || sumCol[k] != diagSum1){
                        return 0;
                    }
                }
                // If all the check's pass, it's a magic square
                return 1;
            };
            // Iterate over each possible 3x3 grid in the grid to count magic squares
            for(int i=0; i<rows; i++){
                for(int j=0; j<cols;j++){
                    magicSquareCount += isMagicSquare(i, j);
                }
            }
            return magicSquareCount; // return the total count of magic courses
        }
};