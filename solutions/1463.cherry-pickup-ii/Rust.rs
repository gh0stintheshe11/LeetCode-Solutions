impl Solution {
    pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        
        // Initialize a 3D DP array with -1 (indicating uncomputed states)
        let mut dp = vec![vec![vec![-1; cols]; cols]; rows];
        
        // Helper function to compute the maximum cherries collected
        fn dfs(grid: &Vec<Vec<i32>>, dp: &mut Vec<Vec<Vec<i32>>>, r: usize, c1: usize, c2: usize) -> i32 {
            let rows = grid.len();
            let cols = grid[0].len();
            
            // If out of bounds, return 0
            if c1 >= cols || c2 >= cols {
                return 0;
            }
            
            // If we have reached the last row
            if r == rows - 1 {
                if c1 == c2 {
                    return grid[r][c1];
                } else {
                    return grid[r][c1] + grid[r][c2];
                }
            }
            
            // If already computed, return the stored value
            if dp[r][c1][c2] != -1 {
                return dp[r][c1][c2];
            }
            
            // Calculate the cherries collected at the current position
            let mut result = grid[r][c1];
            if c1 != c2 {
                result += grid[r][c2];
            }
            
            // Explore all possible moves for both robots
            let mut max_cherries = 0;
            for new_c1 in (c1 as i32 - 1)..=(c1 as i32 + 1) {
                for new_c2 in (c2 as i32 - 1)..=(c2 as i32 + 1) {
                    if new_c1 >= 0 && new_c1 < cols as i32 && new_c2 >= 0 && new_c2 < cols as i32 {
                        max_cherries = max_cherries.max(dfs(grid, dp, r + 1, new_c1 as usize, new_c2 as usize));
                    }
                }
            }
            
            // Store the result in the DP array
            dp[r][c1][c2] = result + max_cherries;
            dp[r][c1][c2]
        }
        
        // Start the DFS from the top row with both robots at their initial positions
        dfs(&grid, &mut dp, 0, 0, cols - 1)
    }
}
