class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        
        int numIslands = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == '1') {
                    ++numIslands;
                    sinkIsland(grid, i, j);
                }
            }
        }

        return numIslands;
    }
    
private:
    void sinkIsland(vector<vector<char>>& grid, int i, int j) {
        if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() || grid[i][j] == '0') {
            return;
        }
        
        grid[i][j] = '0'; // mark the land as visited by sinking it
        sinkIsland(grid, i - 1, j); // up
        sinkIsland(grid, i + 1, j); // down
        sinkIsland(grid, i, j - 1); // left
        sinkIsland(grid, i, j + 1); // right
    }
};