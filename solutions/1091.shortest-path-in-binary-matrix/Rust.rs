use std::collections::VecDeque;

impl Solution {
    pub fn shortest_path_binary_matrix(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if grid[0][0] == 1 || grid[n-1][n-1] == 1 {
            return -1;
        }

        let directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ];

        let mut queue = VecDeque::new();
        queue.push_back((0, 0, 1)); // (row, col, distance)
        grid[0][0] = 1; // Mark as visited

        while let Some((row, col, dist)) = queue.pop_front() {
            if row == n - 1 && col == n - 1 {
                return dist;
            }

            for (dr, dc) in &directions {
                let new_row = row as i32 + dr;
                let new_col = col as i32 + dc;

                if new_row >= 0 && new_row < n as i32 && new_col >= 0 && new_col < n as i32 {
                    let new_row = new_row as usize;
                    let new_col = new_col as usize;
                    if grid[new_row][new_col] == 0 {
                        grid[new_row][new_col] = 1; // Mark as visited
                        queue.push_back((new_row, new_col, dist + 1));
                    }
                }
            }
        }

        -1 // No path found
    }
}