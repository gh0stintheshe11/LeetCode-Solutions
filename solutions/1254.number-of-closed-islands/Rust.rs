impl Solution {
    pub fn closed_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());
        let mut count = 0;

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 0 {
                    if Self::dfs(&mut grid, i, j, m, n) {
                        count += 1;
                    }
                }
            }
        }

        count
    }

    fn dfs(grid: &mut Vec<Vec<i32>>, i: usize, j: usize, m: usize, n: usize) -> bool {
        if i == 0 || i == m - 1 || j == 0 || j == n - 1 {
            return false; // Island touches the border, not closed
        }

        grid[i][j] = 1; // Mark as visited

        let mut is_closed = true;

        for (di, dj) in &[(0, 1), (1, 0), (0, -1), (-1, 0)] {
            let ni = i as i32 + di;
            let nj = j as i32 + dj;
            if ni >= 0 && ni < m as i32 && nj >= 0 && nj < n as i32 {
                let ni = ni as usize;
                let nj = nj as usize;
                if grid[ni][nj] == 0 {
                    is_closed &= Self::dfs(grid, ni, nj, m, n);
                }
            }
        }

        is_closed
    }
}