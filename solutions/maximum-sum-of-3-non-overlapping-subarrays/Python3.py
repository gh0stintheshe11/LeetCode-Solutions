from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_sum = sum(nums[:k])
        w = [0] * (n - k + 1)
        w[0] = max_sum
        for i in range(1, n - k + 1):
            max_sum += nums[i + k - 1] - nums[i - 1]
            w[i] = max_sum
            
        left = [0] * len(w)
        best = 0
        for i in range(len(w)):
            if w[i] > w[best]:
                best = i
            left[i] = best
        
        right = [0] * len(w)
        best = len(w) - 1
        for i in range(len(w) - 1, -1, -1):
            if w[i] >= w[best]:
                best = i
            right[i] = best
            
        ans = None
        for j in range(k, len(w) - k):
            i, l = left[j - k], right[j + k]
            if ans is None or w[i] + w[j] + w[l] > w[ans[0]] + w[ans[1]] + w[ans[2]]:
                ans = [i, j, l]
        return ans