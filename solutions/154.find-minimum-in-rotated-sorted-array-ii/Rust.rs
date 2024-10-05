impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = nums.len() - 1;

        while left < right {
            let mid = left + (right - left) / 2;

            if nums[mid] > nums[right] {
                // The minimum is in the right part
                left = mid + 1;
            } else if nums[mid] < nums[right] {
                // The minimum is in the left part including mid
                right = mid;
            } else {
                // nums[mid] == nums[right], we cannot determine the side, reduce the search space
                right -= 1;
            }
        }

        nums[left]
    }
}
