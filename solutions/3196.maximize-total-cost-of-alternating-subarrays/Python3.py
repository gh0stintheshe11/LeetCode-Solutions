class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp0 = nums[0] + nums[1]
        dp1 = nums[0] - nums[1]
        
        for i in range(2, n):
            new_dp0 = max(dp0, dp1) + nums[i]
            new_dp1 = dp0 - nums[i]
            dp0, dp1 = new_dp0, new_dp1
        
        return max(dp0, dp1)