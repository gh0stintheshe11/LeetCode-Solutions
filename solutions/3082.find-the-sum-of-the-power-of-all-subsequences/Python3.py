class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prevdp = [[0 for s in range(k+1)] for j in range(n+1)]
        prevdp[0][0] = 1
        for i in range(1, n+1):
            dp = [[0 for s in range(k+1)] for j in range(n+1)]
            dp[0][0] = 1
            for j in range(1, n+1):
                for s in range(k+1):
                    dp[j][s] += prevdp[j][s]
                    if s - nums[i-1] >= 0:
                        dp[j][s] += prevdp[j-1][s-nums[i-1]]
            prevdp = dp
        res = 0
        for j in range(1, n+1):
            res += 2**(n-j) * dp[j][k] % (10**9+7)
        return res % (10**9+7)