use std::collections::VecDeque;

impl Solution {
    pub fn shortest_bridge(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut queue = VecDeque::new();
        let mut found = false;

        // Step 1: Find the first island using DFS
        for i in 0..n {
            if found { break; }
            for j in 0..n {
                if grid[i][j] == 1 {
                    Self::dfs(&mut grid, i, j, &mut queue);
                    found = true;
                    break;
                }
            }
        }

        // Step 2: BFS to expand the island
        let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        let mut steps = 0;

        while !queue.is_empty() {
            let size = queue.len();
            for _ in 0..size {
                if let Some((i, j)) = queue.pop_front() {
                    for (di, dj) in &directions {
                        let ni = i as i32 + di;
                        let nj = j as i32 + dj;
                        if ni >= 0 && ni < n as i32 && nj >= 0 && nj < n as i32 {
                            let ni = ni as usize;
                            let nj = nj as usize;
                            if grid[ni][nj] == 1 {
                                return steps;
                            }
                            if grid[ni][nj] == 0 {
                                grid[ni][nj] = 2;
                                queue.push_back((ni, nj));
                            }
                        }
                    }
                }
            }
            steps += 1;
        }

        -1 // Should never reach here given the problem constraints
    }

    fn dfs(grid: &mut Vec<Vec<i32>>, i: usize, j: usize, queue: &mut VecDeque<(usize, usize)>) {
        if i >= grid.len() || j >= grid[0].len() || grid[i][j] != 1 {
            return;
        }
        grid[i][j] = 2;
        queue.push_back((i, j));
        Self::dfs(grid, i + 1, j, queue);
        if i > 0 { Self::dfs(grid, i - 1, j, queue); }
        Self::dfs(grid, i, j + 1, queue);
        if j > 0 { Self::dfs(grid, i, j - 1, queue); }
    }
}