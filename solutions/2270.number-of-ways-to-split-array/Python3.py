class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        valid_splits = 0
        
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            if left_sum >= (total_sum - left_sum):
                valid_splits += 1
        
        return valid_splits