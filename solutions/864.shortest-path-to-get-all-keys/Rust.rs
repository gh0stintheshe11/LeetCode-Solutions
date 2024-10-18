use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn shortest_path_all_keys(grid: Vec<String>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut start = (0, 0);
        let mut total_keys = 0;
        
        // Find starting point and count total keys
        for i in 0..m {
            for j in 0..n {
                if grid[i].chars().nth(j).unwrap() == '@' {
                    start = (i, j);
                } else if grid[i].chars().nth(j).unwrap().is_ascii_lowercase() {
                    total_keys += 1;
                }
            }
        }
        
        let directions = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];
        let mut queue = VecDeque::new();
        let mut visited = HashSet::new();
        
        // (row, col, keys_state, moves)
        queue.push_back((start.0, start.1, 0, 0));
        visited.insert((start.0, start.1, 0));
        
        while let Some((row, col, keys, moves)) = queue.pop_front() {
            if keys == (1 << total_keys) - 1 {
                return moves;
            }
            
            for (dx, dy) in &directions {
                let new_row = row as i32 + dx;
                let new_col = col as i32 + dy;
                
                if new_row >= 0 && new_row < m as i32 && new_col >= 0 && new_col < n as i32 {
                    let new_row = new_row as usize;
                    let new_col = new_col as usize;
                    let cell = grid[new_row].chars().nth(new_col).unwrap();
                    
                    if cell == '#' {
                        continue;
                    }
                    
                    let mut new_keys = keys;
                    
                    if cell.is_ascii_lowercase() {
                        new_keys |= 1 << (cell as u8 - b'a');
                    }
                    
                    if cell.is_ascii_uppercase() && (keys & (1 << (cell as u8 - b'A'))) == 0 {
                        continue;
                    }
                    
                    if !visited.contains(&(new_row, new_col, new_keys)) {
                        visited.insert((new_row, new_col, new_keys));
                        queue.push_back((new_row, new_col, new_keys, moves + 1));
                    }
                }
            }
        }
        
        -1
    }
}