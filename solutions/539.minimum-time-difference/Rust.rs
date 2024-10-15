impl Solution {
    pub fn find_min_difference(time_points: Vec<String>) -> i32 {
        // Convert time points to minutes
        let mut minutes: Vec<i32> = time_points.iter().map(|time| {
            let parts: Vec<&str> = time.split(':').collect();
            let hours: i32 = parts[0].parse().unwrap();
            let mins: i32 = parts[1].parse().unwrap();
            hours * 60 + mins
        }).collect();
        
        // Sort the minutes
        minutes.sort_unstable();
        
        // Initialize the minimum difference to a large number
        let mut min_diff = i32::MAX;
        
        // Calculate the difference between consecutive time points
        for i in 1..minutes.len() {
            let diff = minutes[i] - minutes[i - 1];
            if diff < min_diff {
                min_diff = diff;
            }
        }
        
        // Also consider the circular difference between the last and the first time point
        let circular_diff = 1440 - (minutes[minutes.len() - 1] - minutes[0]);
        if circular_diff < min_diff {
            min_diff = circular_diff;
        }
        
        min_diff
    }
}