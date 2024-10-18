class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        ans, prev = 1, -float('inf')
        prev_max = prev_max_1 = 1
        for x in nums:
            if x == prev:
                prev_max_1 = prev_max + 1
                ans = max(ans, prev_max_1)
                continue
            if x - prev > 2:
                prev_max = prev_max_1 = 1
            elif x == prev + 1:
                prev_max, prev_max_1 = prev_max + 1, prev_max_1 + 1
                ans = max(ans, prev_max, prev_max_1)
            else:
                prev_max, prev_max_1 = prev_max_1 + 1, 1
                ans = max(ans, prev_max)
            prev = x
        return ans