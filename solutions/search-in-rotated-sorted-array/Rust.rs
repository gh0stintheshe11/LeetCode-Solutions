impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len() as i32 - 1;

        while left <= right {
            let mid = left + (right - left) / 2;
            if nums[mid as usize] == target {
                return mid as i32;
            }

            // Determine which part is sorted
            if nums[left as usize] <= nums[mid as usize] {
                // Left part is sorted
                if nums[left as usize] <= target && target < nums[mid as usize] {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right part is sorted
                if nums[mid as usize] < target && target <= nums[right as usize] {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        -1
    }
}
