impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = s.len();
        let s = s.as_bytes();
        
        let mut dp = vec![0; n + 1];
        dp[0] = 1;
        
        for i in 1..=n {
            if s[i - 1] == b'*' {
                dp[i] = (dp[i] + 9 * dp[i - 1]) % MOD;
            } else if s[i - 1] != b'0' {
                dp[i] = (dp[i] + dp[i - 1]) % MOD;
            }
            
            if i > 1 {
                if s[i - 2] == b'*' && s[i - 1] == b'*' {
                    dp[i] = (dp[i] + 15 * dp[i - 2]) % MOD;
                } else if s[i - 2] == b'*' {
                    if s[i - 1] <= b'6' {
                        dp[i] = (dp[i] + 2 * dp[i - 2]) % MOD;
                    } else {
                        dp[i] = (dp[i] + dp[i - 2]) % MOD;
                    }
                } else if s[i - 1] == b'*' {
                    if s[i - 2] == b'1' {
                        dp[i] = (dp[i] + 9 * dp[i - 2]) % MOD;
                    } else if s[i - 2] == b'2' {
                        dp[i] = (dp[i] + 6 * dp[i - 2]) % MOD;
                    }
                } else {
                    let two_digit = (s[i - 2] - b'0') * 10 + (s[i - 1] - b'0');
                    if two_digit >= 10 && two_digit <= 26 {
                        dp[i] = (dp[i] + dp[i - 2]) % MOD;
                    }
                }
            }
        }
        
        dp[n] as i32
    }
}
