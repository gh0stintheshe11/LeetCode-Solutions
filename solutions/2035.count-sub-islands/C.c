#include <stdbool.h>

void dfs(int** grid, int gridSize, int* gridColSize, int x, int y) {
    if (x < 0 || y < 0 || x >= gridSize || y >= gridColSize[x] || grid[x][y] == 0) {
        return;
    }
    grid[x][y] = 0; // Mark the cell as visited
    dfs(grid, gridSize, gridColSize, x + 1, y);
    dfs(grid, gridSize, gridColSize, x - 1, y);
    dfs(grid, gridSize, gridColSize, x, y + 1);
    dfs(grid, gridSize, gridColSize, x, y - 1);
}

bool isSubIsland(int** grid1, int** grid2, int gridSize, int* gridColSize, int x, int y) {
    if (x < 0 || y < 0 || x >= gridSize || y >= gridColSize[x] || grid2[x][y] == 0) {
        return true;
    }
    if (grid1[x][y] == 0) {
        return false;
    }
    grid2[x][y] = 0; // Mark the cell as visited
    bool result = true;
    result &= isSubIsland(grid1, grid2, gridSize, gridColSize, x + 1, y);
    result &= isSubIsland(grid1, grid2, gridSize, gridColSize, x - 1, y);
    result &= isSubIsland(grid1, grid2, gridSize, gridColSize, x, y + 1);
    result &= isSubIsland(grid1, grid2, gridSize, gridColSize, x, y - 1);
    return result;
}

int countSubIslands(int** grid1, int grid1Size, int* grid1ColSize, int** grid2, int grid2Size, int* grid2ColSize) {
    int count = 0;
    for (int i = 0; i < grid2Size; i++) {
        for (int j = 0; j < grid2ColSize[i]; j++) {
            if (grid2[i][j] == 1) {
                if (isSubIsland(grid1, grid2, grid2Size, grid2ColSize, i, j)) {
                    count++;
                } else {
                    dfs(grid2, grid2Size, grid2ColSize, i, j); // Mark the entire island as visited
                }
            }
        }
    }
    return count;
}
