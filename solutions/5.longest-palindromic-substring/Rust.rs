impl Solution {
    /// Finds the longest palindromic substring in the given string.
    ///
    /// # Arguments
    ///
    /// * `s` - A string slice that holds the string to be processed.
    ///
    /// # Returns
    ///
    /// * A string representing the longest palindromic substring.
    pub fn longest_palindrome(s: String) -> String {
        if s.is_empty() {
            return "".to_string();
        }

        let chars: Vec<char> = s.chars().collect();
        let mut start = 0;
        let mut end = 0;

        for i in 0..chars.len() {
            let len1 = Solution::expand_from_center(&chars, i, i);
            let len2 = Solution::expand_from_center(&chars, i, i + 1);
            let len = len1.max(len2);

            if len > (end - start) {
                start = i.saturating_sub((len - 1) / 2);
                end = i + len / 2;
            }
        }

        chars[start..=end].iter().collect()
    }

    /// Expands around the given left and right indices to find the length of the palindrome.
    ///
    /// # Arguments
    ///
    /// * `chars` - A reference to the vector of characters of the string.
    /// * `left` - The left index to start the expansion.
    /// * `right` - The right index to start the expansion.
    ///
    /// # Returns
    ///
    /// * The length of the palindrome found.
    fn expand_from_center(chars: &[char], mut left: usize, mut right: usize) -> usize {
        let n = chars.len();

        // Convert to isize to handle potential underflow when left becomes 0 and we decrement.
        let mut l = left as isize;
        let mut r = right as isize;

        while l >= 0 && r < n as isize && chars[l as usize] == chars[r as usize] {
            l -= 1;
            r += 1;
        }

        // The length is r - l - 1
        (r - l - 1) as usize
    }
}