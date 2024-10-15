class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        return [nums[i] | nums[i + 1] for i in range(len(nums) - 1)]