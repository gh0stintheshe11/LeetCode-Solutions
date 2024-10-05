use std::cmp::max;

impl Solution {
    pub fn longest_valid_parentheses(s: String) -> i32 {
        let mut stack: Vec<i32> = vec![-1];  // Initialize with -1 to handle edge cases
        let mut max_length = 0;

        for (i, ch) in s.chars().enumerate() {
            if ch == '(' {
                stack.push(i as i32);
            } else {  // ch == ')'
                stack.pop();
                if stack.is_empty() {
                    stack.push(i as i32);
                } else {
                    max_length = max(max_length, i as i32 - stack.last().unwrap());
                }
            }
        }

        max_length
    }
}