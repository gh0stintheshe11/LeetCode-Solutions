use std::cmp::max;

impl Solution {
    pub fn max_value(mut events: Vec<Vec<i32>>, k: i32) -> i32 {
        events.sort_unstable_by_key(|e| e[0]);
        let n = events.len();
        let mut dp = vec![vec![-1; k as usize + 1]; n + 1];
        
        Self::dfs(0, k as usize, &events, &mut dp)
    }
    
    fn dfs(i: usize, k: usize, events: &Vec<Vec<i32>>, dp: &mut Vec<Vec<i32>>) -> i32 {
        if i >= events.len() || k == 0 {
            return 0;
        }
        
        if dp[i][k] != -1 {
            return dp[i][k];
        }
        
        // Skip current event
        let skip = Self::dfs(i + 1, k, events, dp);
        
        // Attend current event
        let next_event = Self::binary_search(events, i + 1, events[i][1]);
        let attend = events[i][2] + Self::dfs(next_event, k - 1, events, dp);
        
        dp[i][k] = max(skip, attend);
        dp[i][k]
    }
    
    fn binary_search(events: &Vec<Vec<i32>>, start: usize, target: i32) -> usize {
        let mut left = start;
        let mut right = events.len();
        
        while left < right {
            let mid = left + (right - left) / 2;
            if events[mid][0] <= target {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        left
    }
}