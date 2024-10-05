impl Solution {
    /// Finds the maximum amount of water a container can store.
    ///
    /// # Arguments
    ///
    /// * `height` - A vector of integers representing the heights of the container walls.
    ///
    /// # Returns
    ///
    /// * An integer representing the maximum area of water the container can store.
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left: usize = 0;
        let mut right: usize = height.len() - 1;
        let mut max_area: i32 = 0;

        while left < right {
            // Calculate the height of the container
            let current_height = height[left].min(height[right]);

            // Calculate the width between the two lines
            let width = (right - left) as i32;

            // Calculate the current area
            let current_area = current_height * width;

            // Update max_area if current_area is larger
            if current_area > max_area {
                max_area = current_area;
            }

            // Move the pointer pointing to the shorter line inward
            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }

        max_area
    }
}