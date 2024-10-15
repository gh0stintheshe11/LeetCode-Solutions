class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        total_sum = sum(nums)
        
        if total_sum < 2 * k:
            return 0
        
        n = len(nums)
        
        dp = [0] * k
        dp[0] = 1
        
        for num in nums:
            for current_sum in range(k - 1, num - 1, -1):
                dp[current_sum] = (dp[current_sum] + dp[current_sum - num]) % MOD
        
        count_of_bad_partitions = sum(dp) * 2 % MOD
        total_partitions = pow(2, n, MOD)
        
        result = (total_partitions - count_of_bad_partitions + MOD) % MOD
        
        return result