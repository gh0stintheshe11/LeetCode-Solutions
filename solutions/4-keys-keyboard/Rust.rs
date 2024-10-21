impl Solution {
    pub fn max_a(n: i32) -> i32 {
        let n = n as usize;
        let mut dp = vec![0; n + 1];
        
        for i in 1..=n {
            // Press 'A' directly
            dp[i] = dp[i - 1] + 1;
            
            // Try to use the sequence Ctrl-A, Ctrl-C, followed by multiple Ctrl-V
            for j in 2..i {
                dp[i] = dp[i].max(dp[j - 2] * (i - j + 1));
            }
        }
        
        dp[n] as i32
    }
}
