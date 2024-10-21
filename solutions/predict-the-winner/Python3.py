class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [[None] * n for _ in range(n)]
        
        def dp(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            if i == j:
                return nums[i]
            pick_i = nums[i] - dp(i + 1, j)
            pick_j = nums[j] - dp(i, j - 1)
            memo[i][j] = max(pick_i, pick_j)
            return memo[i][j]
        
        return dp(0, n - 1) >= 0