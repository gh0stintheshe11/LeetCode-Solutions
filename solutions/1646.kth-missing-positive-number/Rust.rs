impl Solution {
    pub fn find_kth_positive(arr: Vec<i32>, k: i32) -> i32 {
        let mut missing_count = 0;
        let mut current = 1;
        let mut index = 0;
        
        while missing_count < k {
            if index < arr.len() && arr[index] == current {
                index += 1;
            } else {
                missing_count += 1;
                if missing_count == k {
                    return current;
                }
            }
            current += 1;
        }
        
        // This line should never be reached because the loop should return the result
        // once missing_count == k.
        current
    }
}
