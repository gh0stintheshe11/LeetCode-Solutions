use std::collections::HashMap;

// Definition for singly-linked list.
// Provided by LeetCode, do not redefine in your submission.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

impl Solution {
    /// Finds the length of the longest substring without repeating characters.
    ///
    /// # Arguments
    ///
    /// * `s` - A string slice that holds the string to be processed.
    ///
    /// # Returns
    ///
    /// * An integer representing the length of the longest substring without repeating characters.
    pub fn length_of_longest_substring(s: String) -> i32 {
        // HashMap to store the latest index of each character.
        let mut char_map: HashMap<char, usize> = HashMap::new();
        let mut max_len = 0;
        let mut start = 0; // Start index of the current window.

        for (i, c) in s.chars().enumerate() {
            if let Some(&prev_index) = char_map.get(&c) {
                // If the character is found in the map and its last index is within the current window.
                if prev_index >= start {
                    // Move the start to one position right of the last occurrence.
                    start = prev_index + 1;
                }
            }
            // Update the latest index of the character.
            char_map.insert(c, i);
            // Calculate the length of the current window and update max_len if necessary.
            let current_len = i - start + 1;
            if current_len > max_len {
                max_len = current_len;
            }
        }

        max_len as i32
    }
}