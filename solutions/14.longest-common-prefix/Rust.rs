impl Solution {
    /// Finds the longest common prefix string amongst an array of strings.
    ///
    /// # Arguments
    ///
    /// * `strs` - A vector of strings to be evaluated.
    ///
    /// # Returns
    ///
    /// * A string representing the longest common prefix. Returns an empty string if no common prefix exists.
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return "".to_string();
        }

        // Find the shortest string in the array
        let min_len = strs.iter().map(|s| s.len()).min().unwrap_or(0);

        let mut prefix = String::new();

        for i in 0..min_len {
            // Get the character at position i from the first string
            let current_char = strs[0].chars().nth(i).unwrap();

            // Check if this character is present at position i in all strings
            for s in &strs[1..] {
                if s.chars().nth(i).unwrap() != current_char {
                    return prefix;
                }
            }

            // If all strings have the same character at position i, append it to the prefix
            prefix.push(current_char);
        }

        prefix
    }
}