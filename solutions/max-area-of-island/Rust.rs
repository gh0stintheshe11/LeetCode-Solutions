impl Solution {
    pub fn max_area_of_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let mut max_area = 0;
        let (m, n) = (grid.len(), grid[0].len());

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    max_area = max_area.max(Self::dfs(&mut grid, i, j));
                }
            }
        }

        max_area
    }

    fn dfs(grid: &mut Vec<Vec<i32>>, i: usize, j: usize) -> i32 {
        if i >= grid.len() || j >= grid[0].len() || grid[i][j] == 0 {
            return 0;
        }

        // Mark the cell as visited by setting it to 0
        grid[i][j] = 0;

        // Explore adjacent cells
        let area = 1 + 
            Self::dfs(grid, i + 1, j) +
            Self::dfs(grid, i.wrapping_sub(1), j) +
            Self::dfs(grid, i, j + 1) +
            Self::dfs(grid, i, j.wrapping_sub(1));

        area
    }
}