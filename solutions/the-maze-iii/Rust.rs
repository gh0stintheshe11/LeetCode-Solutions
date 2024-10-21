use std::collections::{BinaryHeap, HashMap};
use std::cmp::Ordering;

#[derive(Eq, PartialEq)]
struct State {
    dist: i32,
    path: String,
    x: i32,
    y: i32,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.dist.cmp(&self.dist)
            .then_with(|| other.path.cmp(&self.path))
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn find_shortest_way(maze: Vec<Vec<i32>>, ball: Vec<i32>, hole: Vec<i32>) -> String {
        let m = maze.len() as i32;
        let n = maze[0].len() as i32;
        let (start_x, start_y) = (ball[0], ball[1]);
        let (hole_x, hole_y) = (hole[0], hole[1]);
        
        let directions = vec![
            (0, 1, "r"),
            (0, -1, "l"),
            (1, 0, "d"),
            (-1, 0, "u"),
        ];
        
        let mut pq = BinaryHeap::new();
        let mut visited = HashMap::new();
        
        pq.push(State { dist: 0, path: String::new(), x: start_x, y: start_y });
        
        while let Some(State { dist, path, x, y }) = pq.pop() {
            if x == hole_x && y == hole_y {
                return path;
            }
            
            let key = (x, y);
            if let Some(&old_dist) = visited.get(&key) {
                if old_dist < dist {
                    continue;
                }
            }
            visited.insert(key, dist);
            
            for &(dx, dy, dir) in &directions {
                let (mut nx, mut ny) = (x, y);
                let mut nd = dist;
                
                while nx >= 0 && nx < m && ny >= 0 && ny < n && maze[nx as usize][ny as usize] == 0 {
                    if nx == hole_x && ny == hole_y {
                        let mut new_path = path.clone();
                        new_path.push_str(dir);
                        pq.push(State { dist: nd, path: new_path, x: nx, y: ny });
                        break;
                    }
                    nx += dx;
                    ny += dy;
                    nd += 1;
                }
                
                if !(nx == hole_x && ny == hole_y) {
                    nx -= dx;
                    ny -= dy;
                    nd -= 1;
                    if (nx, ny) != (x, y) {
                        let mut new_path = path.clone();
                        new_path.push_str(dir);
                        pq.push(State { dist: nd, path: new_path, x: nx, y: ny });
                    }
                }
            }
        }
        
        "impossible".to_string()
    }
}