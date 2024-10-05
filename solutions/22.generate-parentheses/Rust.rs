impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        fn backtrack(result: &mut Vec<String>, current: &mut String, open: i32, close: i32, max: i32) {
            if current.len() == (max * 2) as usize {
                result.push(current.clone());
                return;
            }
            
            if open < max {
                current.push('(');
                backtrack(result, current, open + 1, close, max);
                current.pop();
            }
            
            if close < open {
                current.push(')');
                backtrack(result, current, open, close + 1, max);
                current.pop();
            }
        }
        
        let mut result = Vec::new();
        let mut current = String::new();
        backtrack(&mut result, &mut current, 0, 0, n);
        result
    }
}
