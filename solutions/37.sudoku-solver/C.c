void solveSudoku(char** board, int boardSize, int* boardColSize) {
    // Arrays to keep track of used numbers
    int rows[9][10] = {0};   // rows[i][num] == 1 if num is used in row i
    int cols[9][10] = {0};   // cols[j][num] == 1 if num is used in column j
    int boxes[9][10] = {0};  // boxes[box_index][num] == 1 if num is used in box

    // Initialize the used numbers based on the initial board state
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            char c = board[i][j];
            if (c != '.') {
                int num = c - '0';
                int box_index = (i / 3) * 3 + j / 3;
                rows[i][num] = 1;
                cols[j][num] = 1;
                boxes[box_index][num] = 1;
            }
        }
    }

    // Start solving from the first cell
    solve(board, 0, 0, rows, cols, boxes);
}

int solve(char** board, int row, int col, int rows[9][10], int cols[9][10], int boxes[9][10]) {
    // If we've reached the end of the board, puzzle is solved
    if (row == 9)
        return 1;

    // Move to the next row if we've reached the end of the current row
    if (col == 9)
        return solve(board, row + 1, 0, rows, cols, boxes);

    // If the cell is already filled, move to the next cell
    if (board[row][col] != '.')
        return solve(board, row, col + 1, rows, cols, boxes);

    // Try digits from '1' to '9'
    for (int num = 1; num <= 9; num++) {
        int box_index = (row / 3) * 3 + col / 3;
        if (!rows[row][num] && !cols[col][num] && !boxes[box_index][num]) {
            // Place the number
            board[row][col] = num + '0';
            rows[row][num] = 1;
            cols[col][num] = 1;
            boxes[box_index][num] = 1;

            // Recursively solve for the next cell
            if (solve(board, row, col + 1, rows, cols, boxes))
                return 1;

            // Backtrack
            board[row][col] = '.';
            rows[row][num] = 0;
            cols[col][num] = 0;
            boxes[box_index][num] = 0;
        }
    }

    // No valid number found, trigger backtracking
    return 0;
}
