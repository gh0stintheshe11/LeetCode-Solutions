impl Solution {
    pub fn count_sub_islands(grid1: Vec<Vec<i32>>, grid2: Vec<Vec<i32>>) -> i32 {
        let mut grid2 = grid2.clone();
        let m = grid1.len();
        let n = grid1[0].len();
        let mut count = 0;

        fn dfs(grid1: &Vec<Vec<i32>>, grid2: &mut Vec<Vec<i32>>, i: usize, j: usize) -> bool {
            if i >= grid1.len() || j >= grid1[0].len() || grid2[i][j] == 0 {
                return true;
            }
            if grid1[i][j] == 0 {
                return false;
            }
            grid2[i][j] = 0; // Mark the cell as visited
            let mut is_sub_island = true;
            let directions = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];
            for (di, dj) in directions {
                let ni = i as isize + di;
                let nj = j as isize + dj;
                if ni >= 0 && ni < grid1.len() as isize && nj >= 0 && nj < grid1[0].len() as isize {
                    is_sub_island &= dfs(grid1, grid2, ni as usize, nj as usize);
                }
            }
            is_sub_island
        }

        for i in 0..m {
            for j in 0..n {
                if grid2[i][j] == 1 {
                    if dfs(&grid1, &mut grid2, i, j) {
                        count += 1;
                    }
                }
            }
        }

        count
    }
}
