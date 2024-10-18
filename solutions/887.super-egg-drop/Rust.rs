impl Solution {
    pub fn super_egg_drop(k: i32, n: i32) -> i32 {
        let mut dp = vec![vec![0; k as usize + 1]; n as usize + 1];
        let mut m = 0;
        
        while dp[m][k as usize] < n {
            m += 1;
            for i in 1..=k as usize {
                dp[m][i] = dp[m-1][i-1] + dp[m-1][i] + 1;
            }
        }
        
        m as i32
    }
}