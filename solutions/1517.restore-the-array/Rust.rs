impl Solution {
    pub fn number_of_arrays(s: String, k: i32) -> i32 {
        let n = s.len();
        let k = k as i64;
        let s = s.as_bytes();
        let modulo = 1_000_000_007;
        
        // dp[i] will store the number of ways to partition the substring s[i..]
        let mut dp = vec![0; n + 1];
        dp[n] = 1; // Base case: there's one way to partition an empty substring
        
        for i in (0..n).rev() {
            if s[i] == b'0' {
                dp[i] = 0; // No valid number can start with '0'
                continue;
            }
            
            let mut num = 0;
            for j in i..n {
                num = num * 10 + (s[j] - b'0') as i64;
                if num > k {
                    break;
                }
                dp[i] = (dp[i] + dp[j + 1]) % modulo;
            }
        }
        
        dp[0]
    }
}
