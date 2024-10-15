from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return (1 - 0) * nums[1]
        
        suffixMax = [(0, 0)] * n
        suffixMax[-1] = (nums[-1], n - 1)
        
        for i in range(n - 2, -1, -1):
            if nums[i] > suffixMax[i + 1][0]:
                suffixMax[i] = (nums[i], i)
            else:
                suffixMax[i] = suffixMax[i + 1]
        
        maxScore = 0
        i = 0
        
        while i < n - 1:
            maxValue, j = suffixMax[i + 1]
            maxScore += (j - i) * maxValue
            i = j
        
        return maxScore