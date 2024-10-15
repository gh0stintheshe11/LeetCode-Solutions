impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        if num < 1 {
            return false;
        }
        
        let mut left = 1;
        let mut right = num;
        
        while left <= right {
            let mid = left + (right - left) / 2;
            let mid_squared = mid as i64 * mid as i64; // Use i64 to prevent overflow
            
            if mid_squared == num as i64 {
                return true;
            } else if mid_squared < num as i64 {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        false
    }
}
