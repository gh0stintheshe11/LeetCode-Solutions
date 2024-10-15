class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                operations += len(nums) - i
        return operations