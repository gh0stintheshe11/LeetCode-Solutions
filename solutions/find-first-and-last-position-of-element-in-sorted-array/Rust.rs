impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        fn find_first(nums: &Vec<i32>, target: i32) -> i32 {
            let mut left = 0;
            let mut right = nums.len() as i32 - 1;
            let mut result = -1;
            
            while left <= right {
                let mid = left + (right - left) / 2;
                if nums[mid as usize] == target {
                    result = mid;
                    right = mid - 1; // continue searching in the left half
                } else if nums[mid as usize] < target {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            
            result
        }
        
        fn find_last(nums: &Vec<i32>, target: i32) -> i32 {
            let mut left = 0;
            let mut right = nums.len() as i32 - 1;
            let mut result = -1;
            
            while left <= right {
                let mid = left + (right - left) / 2;
                if nums[mid as usize] == target {
                    result = mid;
                    left = mid + 1; // continue searching in the right half
                } else if nums[mid as usize] < target {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            
            result
        }
        
        let first = find_first(&nums, target);
        if first == -1 {
            return vec![-1, -1];
        }
        
        let last = find_last(&nums, target);
        vec![first, last]
    }
}
