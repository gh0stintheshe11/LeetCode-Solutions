impl Solution {
    pub fn num_enclaves(mut grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());

        // Mark land cells connected to boundary
        for i in 0..m {
            Self::dfs(&mut grid, i, 0);
            Self::dfs(&mut grid, i, n - 1);
        }
        for j in 0..n {
            Self::dfs(&mut grid, 0, j);
            Self::dfs(&mut grid, m - 1, j);
        }

        // Count remaining land cells
        grid.iter().flatten().filter(|&&cell| cell == 1).count() as i32
    }

    fn dfs(grid: &mut Vec<Vec<i32>>, i: usize, j: usize) {
        if i >= grid.len() || j >= grid[0].len() || grid[i][j] != 1 {
            return;
        }

        grid[i][j] = 0; // Mark as visited

        // Check adjacent cells
        Self::dfs(grid, i + 1, j);
        if i > 0 { Self::dfs(grid, i - 1, j); }
        Self::dfs(grid, i, j + 1);
        if j > 0 { Self::dfs(grid, i, j - 1); }
    }
}