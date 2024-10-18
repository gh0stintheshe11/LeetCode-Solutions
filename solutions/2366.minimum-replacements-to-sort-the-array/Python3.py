class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        n = len(nums)
        prev_bound = nums[-1]
        
        for i in range(n - 2, -1, -1):
            if nums[i] > prev_bound:
                times = (nums[i] + prev_bound - 1) // prev_bound
                operations += times - 1
                prev_bound = nums[i] // times
            else:
                prev_bound = nums[i]
        
        return operations