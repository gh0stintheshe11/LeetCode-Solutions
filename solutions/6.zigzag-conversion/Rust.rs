impl Solution {
    /// Converts the given string `s` into a zigzag pattern on `num_rows` rows
    /// and returns the string read line by line.
    ///
    /// # Arguments
    ///
    /// * `s` - The input string to be converted.
    /// * `num_rows` - The number of rows for the zigzag pattern.
    ///
    /// # Returns
    ///
    /// * A string representing the zigzag-converted string.
    pub fn convert(s: String, num_rows: i32) -> String {
        // Edge case: if num_rows is 1 or greater than the length of s,
        // the zigzag pattern is the same as the original string.
        if num_rows == 1 || num_rows as usize >= s.len() {
            return s;
        }

        // Initialize a vector of empty strings for each row.
        let mut rows: Vec<String> = vec![String::new(); num_rows as usize];
        let mut current_row: usize = 0;
        let mut going_down: bool = false;

        // Iterate over each character in the string.
        for c in s.chars() {
            // Append the current character to the current row.
            rows[current_row].push(c);

            // If we're at the top or bottom row, change direction.
            if current_row == 0 || current_row == (num_rows as usize - 1) {
                going_down = !going_down;
            }

            // Update the current row based on the direction.
            if going_down {
                current_row += 1;
            } else {
                current_row -= 1;
            }
        }

        // Concatenate all rows to form the final string.
        rows.concat()
    }
}