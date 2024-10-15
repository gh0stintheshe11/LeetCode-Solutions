from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_so_far = nums[0]
        score = 0
        ans = []
        for i in range(n):
            max_so_far = max(max_so_far, nums[i])
            score += nums[i] + max_so_far
            ans.append(score)
        return ans