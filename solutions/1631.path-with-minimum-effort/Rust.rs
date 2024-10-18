use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        let rows = heights.len();
        let cols = heights[0].len();
        
        let directions = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];
        
        let mut left = 0;
        let mut right = 1_000_000;
        
        while left < right {
            let mid = (left + right) / 2;
            if Self::can_reach_end(&heights, mid, &directions) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        left
    }
    
    fn can_reach_end(heights: &Vec<Vec<i32>>, max_effort: i32, directions: &Vec<(i32, i32)>) -> bool {
        let rows = heights.len();
        let cols = heights[0].len();
        let mut visited = vec![vec![false; cols]; rows];
        let mut heap = BinaryHeap::new();
        
        heap.push(Reverse((0, 0, 0))); // (effort, row, col)
        
        while let Some(Reverse((effort, row, col))) = heap.pop() {
            if row == rows - 1 && col == cols - 1 {
                return true;
            }
            
            if visited[row][col] {
                continue;
            }
            
            visited[row][col] = true;
            
            for &(dr, dc) in directions.iter() {
                let new_row = row as i32 + dr;
                let new_col = col as i32 + dc;
                
                if new_row >= 0 && new_row < rows as i32 && new_col >= 0 && new_col < cols as i32 {
                    let new_row = new_row as usize;
                    let new_col = new_col as usize;
                    let new_effort = (heights[new_row][new_col] - heights[row][col]).abs();
                    
                    if new_effort <= max_effort && !visited[new_row][new_col] {
                        heap.push(Reverse((new_effort, new_row, new_col)));
                    }
                }
            }
        }
        
        false
    }
}
