from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        answer = []
        
        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]
            answer.append(abs(left_sum - right_sum))
            left_sum += nums[i]
        
        return answer