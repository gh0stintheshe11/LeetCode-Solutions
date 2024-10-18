class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        min_value = float('inf')
        
        for i in range(len(nums) - 1):
            min_value = min(min_value, nums[i + 1] - nums[i])
        
        return min_value