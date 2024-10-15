class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        n = len(nums)
        
        max_score = float('-inf')
        prefix_sum = 0
        
        for i in range(n):
            prefix_sum += nums[i]
            suffix_sum = total_sum - prefix_sum + nums[i]
            max_score = max(max_score, prefix_sum, suffix_sum)
        
        return max_score