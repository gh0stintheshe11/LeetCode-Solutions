class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))
        max_F = F
        
        for i in range(1, n):
            F += sum_nums - n * nums[n - i]
            max_F = max(max_F, F)
        
        return max_F