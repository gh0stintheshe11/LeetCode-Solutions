class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        
        // Directions for the eight neighbors
        vector<vector<int>> directions = {{-1, -1}, {-1, 0}, {-1, 1}, 
                                          {0, -1}, {0, 1},
                                          {1, -1}, {1, 0}, {1, 1}};
        
        // Iterate through each cell in the board
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int liveNeighbors = 0;
                
                // Count live neighbors
                for (auto dir : directions) {
                    int ni = i + dir[0];
                    int nj = j + dir[1];
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                        // Check 1 and 2 means the cell was live in the previous state
                        if (board[ni][nj] == 1 || board[ni][nj] == 2) {
                            liveNeighbors++;
                        }
                    }
                }
                
                // Rule 1 and 3: live cell dies due to under/over-population
                if (board[i][j] == 1 && (liveNeighbors < 2 || liveNeighbors > 3)) {
                    board[i][j] = 2; // Mark as transitioned from live -> dead
                }
                
                // Rule 4: dead cell becomes live
                if (board[i][j] == 0 && liveNeighbors == 3) {
                    board[i][j] = 3; // Mark as transitioned from dead -> live
                }
            }
        }
        
        // Finalize the next state
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == 2) {
                    board[i][j] = 0; // Now dead
                } else if (board[i][j] == 3) {
                    board[i][j] = 1; // Now live
                }
            }
        }
    }
};