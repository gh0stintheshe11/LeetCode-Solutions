use std::collections::VecDeque;

impl Solution {
    pub fn nearest_exit(maze: Vec<Vec<char>>, entrance: Vec<i32>) -> i32 {
        let (m, n) = (maze.len(), maze[0].len());
        let (start_row, start_col) = (entrance[0] as usize, entrance[1] as usize);
        let mut queue = VecDeque::new();
        let mut visited = vec![vec![false; n]; m];
        let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)];

        // Start BFS from the entrance
        queue.push_back((start_row, start_col, 0));
        visited[start_row][start_col] = true;

        while let Some((row, col, steps)) = queue.pop_front() {
            // Check if we've reached an exit
            if (row == 0 || row == m - 1 || col == 0 || col == n - 1) && 
               (row != start_row || col != start_col) {
                return steps;
            }

            // Explore neighboring cells
            for (dr, dc) in &directions {
                let new_row = row as i32 + dr;
                let new_col = col as i32 + dc;

                if new_row >= 0 && new_row < m as i32 && new_col >= 0 && new_col < n as i32 {
                    let new_row = new_row as usize;
                    let new_col = new_col as usize;

                    if !visited[new_row][new_col] && maze[new_row][new_col] == '.' {
                        queue.push_back((new_row, new_col, steps + 1));
                        visited[new_row][new_col] = true;
                    }
                }
            }
        }

        -1 // No exit found
    }
}