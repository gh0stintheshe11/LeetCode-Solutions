impl Solution {
    /// Reverses the digits of a 32-bit signed integer.
    ///
    /// # Arguments
    ///
    /// * `x` - A 32-bit signed integer to be reversed.
    ///
    /// # Returns
    ///
    /// * The reversed integer if it fits within the 32-bit signed integer range; otherwise, `0`.
    pub fn reverse(x: i32) -> i32 {
        let mut rev: i32 = 0;
        let mut x = x; // Make `x` mutable to modify it within the loop.

        while x != 0 {
            // Extract the last digit.
            let pop = x % 10;
            x /= 10;

            // Check for overflow before actually appending the digit.
            // i32::MAX = 2147483647, i32::MIN = -2147483648
            if rev > i32::MAX / 10 || (rev == i32::MAX / 10 && pop > 7) {
                return 0;
            }
            if rev < i32::MIN / 10 || (rev == i32::MIN / 10 && pop < -8) {
                return 0;
            }

            // Append the digit.
            rev = rev * 10 + pop;
        }

        rev
    }
}