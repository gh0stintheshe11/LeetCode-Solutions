impl Solution {
    pub unsafe fn guessNumber(n: i32) -> i32 {
        let mut left = 1;
        let mut right = n;
        
        while left <= right {
            let mid = left + (right - left) / 2;
            match guess(mid) {
                -1 => right = mid - 1,
                1 => left = mid + 1,
                0 => return mid,
                _ => unreachable!(),
            }
        }
        
        // If the function reaches here, it means the number was not found,
        // which should not happen given the problem constraints.
        unreachable!()
    }
}
