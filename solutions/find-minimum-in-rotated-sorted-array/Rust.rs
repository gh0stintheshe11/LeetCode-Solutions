impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = nums.len() - 1;

        while left < right {
            let mid = left + (right - left) / 2;

            // If the middle element is greater than the rightmost element,
            // the minimum must be to the right of mid.
            if nums[mid] > nums[right] {
                left = mid + 1;
            } else {
                // Otherwise, the minimum is to the left of mid (including mid).
                right = mid;
            }
        }

        // After the loop, left == right and it points to the minimum element.
        nums[left]
    }
}
