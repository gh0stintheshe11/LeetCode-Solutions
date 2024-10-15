class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7
        
        def digit_dp(s, is_tight, pos, sum_so_far, min_sum, max_sum, dp):
            if sum_so_far > max_sum:
                return 0
            if pos == len(s):
                return min_sum <= sum_so_far <= max_sum
            if dp[is_tight][pos][sum_so_far] != -1:
                return dp[is_tight][pos][sum_so_far]
            
            limit = int(s[pos]) if is_tight else 9
            count = 0
            for digit in range(0, limit + 1):
                count += digit_dp(s, is_tight and (digit == limit), pos + 1, sum_so_far + digit, min_sum, max_sum, dp)
                count %= MOD
            
            dp[is_tight][pos][sum_so_far] = count
            return count
        
        def f(n, min_sum, max_sum):
            dp = [[[-1] * (max_sum + 1) for _ in range(len(n) + 1)] for _ in range(2)]
            return digit_dp(n, True, 0, 0, min_sum, max_sum, dp)
        
        # The subtraction of '1' ensures properly handling inclusive counting
        num1 = str(int(num1) - 1)
        
        count_num2 = f(num2, min_sum, max_sum)
        count_num1 = f(num1, min_sum, max_sum)
        
        return (count_num2 - count_num1 + MOD) % MOD