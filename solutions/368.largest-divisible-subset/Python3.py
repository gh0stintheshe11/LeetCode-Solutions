from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        dp = [(1, -1, num) for num in nums]
        max_size = 0
        max_index = 0
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i][0] < dp[j][0] + 1:
                    dp[i] = (dp[j][0] + 1, j, nums[i])
            if dp[i][0] > max_size:
                max_size, max_index = dp[i][0], i

        result = []
        while max_index != -1:
            result.append(dp[max_index][2])
            max_index = dp[max_index][1]
        
        return result[::-1]