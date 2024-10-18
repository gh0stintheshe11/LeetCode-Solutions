from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = [0] * 1001
        
        def backtrack(index: int) -> int:
            if index == len(nums):
                return 1

            res = backtrack(index + 1)

            if cnt[nums[index] - k] == 0:
                cnt[nums[index]] += 1
                res += backtrack(index + 1)
                cnt[nums[index]] -= 1

            return res

        return backtrack(0) - 1