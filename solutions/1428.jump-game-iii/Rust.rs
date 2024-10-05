use std::collections::VecDeque;

impl Solution {
    pub fn can_reach(arr: Vec<i32>, start: i32) -> bool {
        let n = arr.len();
        let mut visited = vec![false; n];
        let mut queue = VecDeque::new();
        
        queue.push_back(start as usize);
        visited[start as usize] = true;
        
        while let Some(i) = queue.pop_front() {
            if arr[i] == 0 {
                return true;
            }
            
            let left = i as i32 - arr[i];
            let right = i as i32 + arr[i];
            
            for &next in &[left, right] {
                if next >= 0 && next < n as i32 && !visited[next as usize] {
                    queue.push_back(next as usize);
                    visited[next as usize] = true;
                }
            }
        }
        
        false
    }
}