impl Solution {
    pub fn largest_perimeter(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort_unstable(); // Sort the array in non-decreasing order
        
        // Iterate from the end to the beginning
        for i in (2..nums.len()).rev() {
            if nums[i] < nums[i - 1] + nums[i - 2] {
                // If the sum of the two smaller sides is greater than the largest side
                return nums[i] + nums[i - 1] + nums[i - 2];
            }
        }
        
        // If no valid triangle is found, return 0
        0
    }
}
