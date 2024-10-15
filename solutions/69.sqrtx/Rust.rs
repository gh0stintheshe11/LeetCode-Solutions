impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        if x < 2 {
            return x;
        }

        let mut left = 1;
        let mut right = x / 2;
        let mut result = 0;

        while left <= right {
            let mid = left + (right - left) / 2;
            let mid_squared = mid as i64 * mid as i64;

            if mid_squared == x as i64 {
                return mid;
            } else if mid_squared < x as i64 {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        result
    }
}
