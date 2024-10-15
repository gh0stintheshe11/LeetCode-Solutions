impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        // Calculate the total number of integers in the range
        let total_numbers = high - low + 1;
        
        // If the total number of integers is even
        if total_numbers % 2 == 0 {
            return total_numbers / 2;
        } else {
            // If the total number of integers is odd
            // Check if either low or high is odd
            if low % 2 == 1 || high % 2 == 1 {
                return total_numbers / 2 + 1;
            } else {
                return total_numbers / 2;
            }
        }
    }
}
