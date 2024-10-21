class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort(reverse=True)
        
        score = 0
        m = len(nums[0])
        
        for j in range(m):
            max_value = 0
            for i in range(len(nums)):
                max_value = max(max_value, nums[i][j])
            score += max_value
        
        return score