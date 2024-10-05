use std::collections::{BinaryHeap, HashMap};
use std::cmp::Reverse;

impl Solution {
    pub fn shortest_distance(maze: Vec<Vec<i32>>, start: Vec<i32>, destination: Vec<i32>) -> i32 {
        let m = maze.len();
        let n = maze[0].len();
        let (start_row, start_col) = (start[0] as usize, start[1] as usize);
        let (dest_row, dest_col) = (destination[0] as usize, destination[1] as usize);
        
        let mut distances = HashMap::new();
        let mut pq = BinaryHeap::new();
        
        pq.push(Reverse((0, start_row, start_col)));
        distances.insert((start_row, start_col), 0);
        
        let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        
        while let Some(Reverse((dist, row, col))) = pq.pop() {
            if row == dest_row && col == dest_col {
                return dist;
            }
            
            if dist > *distances.get(&(row, col)).unwrap_or(&i32::MAX) {
                continue;
            }
            
            for &(dx, dy) in &directions {
                let (mut new_row, mut new_col) = (row as i32, col as i32);
                let mut steps = 0;
                
                while new_row >= 0 && new_row < m as i32 && new_col >= 0 && new_col < n as i32 
                      && maze[new_row as usize][new_col as usize] == 0 {
                    new_row += dx;
                    new_col += dy;
                    steps += 1;
                }
                
                new_row -= dx;
                new_col -= dy;
                steps -= 1;
                
                let new_dist = dist + steps;
                if new_dist < *distances.get(&(new_row as usize, new_col as usize)).unwrap_or(&i32::MAX) {
                    distances.insert((new_row as usize, new_col as usize), new_dist);
                    pq.push(Reverse((new_dist, new_row as usize, new_col as usize)));
                }
            }
        }
        
        -1
    }
}