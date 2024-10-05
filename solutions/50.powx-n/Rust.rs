impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        // Helper function to handle the power calculation
        fn pow(x: f64, n: i64) -> f64 {
            if n == 0 {
                return 1.0;
            }
            let half = pow(x, n / 2);
            if n % 2 == 0 {
                half * half
            } else {
                half * half * x
            }
        }

        // Handle the case where n is negative
        let n = n as i64;
        if n < 0 {
            1.0 / pow(x, -n)
        } else {
            pow(x, n)
        }
    }
}
