impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        let n = citations.len();
        let mut left = 0;
        let mut right = n as i32 - 1;
        
        while left <= right {
            let mid = left + (right - left) / 2;
            if citations[mid as usize] >= (n as i32 - mid) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        (n as i32 - left) as i32
    }
}
