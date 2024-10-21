from typing import List
from bisect import bisect_left

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        keys = []
        tree = [0] * (n + 1)

        def query(x):
            result = 0
            while x:
                result = max(result, tree[x])
                x -= x & -x
            return result

        def update(x, val):
            while x <= n:
                tree[x] = max(tree[x], val)
                x += x & -x

        for i in range(n):
            keys.append(nums[i] - i)
        keys.sort()

        result = float('-inf')
        for i in range(n):
            index = bisect_left(keys, nums[i] - i)
            dp[i] = max(nums[i], nums[i] + query(index + 1))
            update(index + 1, dp[i])
            result = max(result, dp[i])

        return result