impl Solution {
    pub fn find_right_interval(intervals: Vec<Vec<i32>>) -> Vec<i32> {
        use std::cmp::Ordering;
        
        // Create a vector of tuples (start, index) and sort it by start
        let mut starts: Vec<(i32, usize)> = intervals.iter()
            .enumerate()
            .map(|(i, interval)| (interval[0], i))
            .collect();
        starts.sort_by(|a, b| a.0.cmp(&b.0));
        
        // Function to perform binary search to find the right interval
        fn binary_search(starts: &[(i32, usize)], target: i32) -> i32 {
            let mut left = 0;
            let mut right = starts.len();
            while left < right {
                let mid = left + (right - left) / 2;
                if starts[mid].0 >= target {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            if left < starts.len() {
                starts[left].1 as i32
            } else {
                -1
            }
        }
        
        // Result vector
        let mut result = vec![-1; intervals.len()];
        
        // Find the right interval for each interval
        for (i, interval) in intervals.iter().enumerate() {
            let end = interval[1];
            result[i] = binary_search(&starts, end);
        }
        
        result
    }
}
