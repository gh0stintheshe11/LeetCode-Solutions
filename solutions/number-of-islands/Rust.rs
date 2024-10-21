impl Solution {
    pub fn num_islands(mut grid: Vec<Vec<char>>) -> i32 {
        let mut count = 0;
        let (m, n) = (grid.len(), grid[0].len());

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == '1' {
                    Self::dfs(&mut grid, i, j);
                    count += 1;
                }
            }
        }

        count
    }

    fn dfs(grid: &mut Vec<Vec<char>>, i: usize, j: usize) {
        if i >= grid.len() || j >= grid[0].len() || grid[i][j] != '1' {
            return;
        }

        grid[i][j] = '0'; // Mark as visited

        // Check adjacent cells
        Self::dfs(grid, i + 1, j);
        if i > 0 { Self::dfs(grid, i - 1, j); }
        Self::dfs(grid, i, j + 1);
        if j > 0 { Self::dfs(grid, i, j - 1); }
    }
}