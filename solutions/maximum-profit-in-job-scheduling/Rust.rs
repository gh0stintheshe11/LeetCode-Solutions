use std::cmp::max;

impl Solution {
    pub fn job_scheduling(start_time: Vec<i32>, end_time: Vec<i32>, profit: Vec<i32>) -> i32 {
        let n = start_time.len();
        let mut jobs: Vec<(i32, i32, i32)> = start_time.into_iter()
            .zip(end_time.into_iter())
            .zip(profit.into_iter())
            .map(|((s, e), p)| (s, e, p))
            .collect();
        
        jobs.sort_unstable_by_key(|&(_, e, _)| e);
        
        let mut dp = vec![0; n];
        dp[0] = jobs[0].2;
        
        for i in 1..n {
            let profit = jobs[i].2;
            let last_non_overlap = Self::binary_search(&jobs, i, jobs[i].0);
            
            dp[i] = max(profit + if last_non_overlap != -1 { dp[last_non_overlap as usize] } else { 0 },
                        dp[i-1]);
        }
        
        *dp.last().unwrap()
    }
    
    fn binary_search(jobs: &[(i32, i32, i32)], end: usize, target: i32) -> i32 {
        let mut low = 0;
        let mut high = end as i32 - 1;
        
        while low <= high {
            let mid = low + (high - low) / 2;
            if jobs[mid as usize].1 <= target {
                if mid == end as i32 - 1 || jobs[(mid + 1) as usize].1 > target {
                    return mid;
                }
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        -1
    }
}