impl Solution {
    /// Converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
    ///
    /// # Arguments
    ///
    /// * `s` - A string slice that holds the string to be converted.
    ///
    /// # Returns
    ///
    /// * An integer representing the converted 32-bit signed integer. Returns 0 if the conversion
    ///   leads to an overflow or if no valid conversion could be performed.
    pub fn my_atoi(s: String) -> i32 {
        let mut chars = s.chars().peekable();
        let mut sign: i32 = 1;
        let mut rev: i32 = 0;

        // Step 1: Ignore leading whitespaces
        while let Some(&c) = chars.peek() {
            if c == ' ' {
                chars.next();
            } else {
                break;
            }
        }

        // Step 2: Check for sign
        if let Some(&c) = chars.peek() {
            if c == '-' {
                sign = -1;
                chars.next();
            } else if c == '+' {
                chars.next();
            }
        }

        // Step 3: Convert digits to integer
        while let Some(c) = chars.next() {
            if !c.is_digit(10) {
                break;
            }

            let digit = (c as u8 - b'0') as i32;

            // Step 4: Check for overflow/underflow
            if sign == 1 {
                if rev > (i32::MAX - digit) / 10 {
                    return i32::MAX;
                }
            } else {
                if rev < (i32::MIN + digit) / 10 {
                    return i32::MIN;
                }
            }

            // Append the digit with consideration of the sign
            rev = rev * 10 + sign * digit;
        }

        rev
    }
}