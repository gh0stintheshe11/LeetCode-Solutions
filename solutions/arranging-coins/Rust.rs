impl Solution {
    pub fn arrange_coins(n: i32) -> i32 {
        let n = n as i64; // Convert to i64 to handle large values
        let k = ((-1.0 + (1.0 + 8.0 * n as f64).sqrt()) / 2.0).floor() as i32;
        k
    }
}
