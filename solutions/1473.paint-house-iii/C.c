#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

int minCost(int* houses, int housesSize, int** cost, int costSize, int* costColSize, int m, int n, int target) {
    // Initialize the DP array with a large value (infinity)
    int dp[m][n][target + 1];
    memset(dp, 0x3f, sizeof(dp));
    
    // If the first house is already painted
    if (houses[0] != 0) {
        dp[0][houses[0] - 1][1] = 0;
    } else {
        for (int j = 0; j < n; ++j) {
            dp[0][j][1] = cost[0][j];
        }
    }
    
    // Fill the DP table
    for (int i = 1; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (houses[i] != 0 && houses[i] - 1 != j) continue;
            for (int k = 1; k <= target; ++k) {
                int currentCost = (houses[i] == 0) ? cost[i][j] : 0;
                for (int p = 0; p < n; ++p) {
                    if (p == j) {
                        dp[i][j][k] = MIN(dp[i][j][k], dp[i - 1][j][k] + currentCost);
                    } else {
                        dp[i][j][k] = MIN(dp[i][j][k], dp[i - 1][p][k - 1] + currentCost);
                    }
                }
            }
        }
    }
    
    // Find the minimum cost with exactly target neighborhoods
    int result = INT_MAX;
    for (int j = 0; j < n; ++j) {
        result = MIN(result, dp[m - 1][j][target]);
    }
    
    return (result == 0x3f3f3f3f) ? -1 : result;
}

// Helper function to create a 2D array
int** create2DArray(int rows, int cols) {
    int** array = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; ++i) {
        array[i] = (int*)malloc(cols * sizeof(int));
    }
    return array;
}

// Helper function to free a 2D array
void free2DArray(int** array, int rows) {
    for (int i = 0; i < rows; ++i) {
        free(array[i]);
    }
    free(array);
}
