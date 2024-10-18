class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        @cache
        def dp(i, j, prev):
            if i == len(nums) and j == len(andValues): return 0
            if i == len(nums) or j == len(andValues) or prev&nums[i] < andValues[j]: return 10**10
            if prev&nums[i] == andValues[j]:
                return min(dp(i+1, j, prev&nums[i]), dp(i+1, j+1, (1<<31)-1)+nums[i])
            else:
                return dp(i+1, j, prev&nums[i])
        return dp(0, 0, (1<<31)-1) if dp(0, 0, (1<<31)-1) < 10**9 else -1