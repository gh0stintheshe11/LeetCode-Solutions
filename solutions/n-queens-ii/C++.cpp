class Solution {
public:
    int totalNQueens(int n) {
        return solveNQueensHelper(n, 0, 0, 0, 0);
    }
    
private:
    int solveNQueensHelper(int n, int row, int cols, int d1, int d2) {
        if (row == n) return 1;
        int count = 0;
        int availablePositions = ((1 << n) - 1) & ~(cols | d1 | d2);
        while (availablePositions) {
            int position = availablePositions & -availablePositions;
            availablePositions &= availablePositions - 1;
            count += solveNQueensHelper(n, row + 1, cols | position, 
                                        (d1 | position) << 1, 
                                        (d2 | position) >> 1);
        }
        return count;
    }
};