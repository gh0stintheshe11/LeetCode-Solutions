from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prefix_sum = 0
        score = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum > 0:
                score += 1
            else:
                break

        return score