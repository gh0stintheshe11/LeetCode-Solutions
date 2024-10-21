class Solution:
    
    def minLargest(self, nums1, nums2):
        from itertools import product
        from math import inf

        incr = lambda x, y: x + 1 + (x % 2 == y % 2)

        n1, n2 = len(nums1), len(nums2)
        dp = [[inf] * (n2 + 1) for _ in range(n1 + 1)]

        dp[0][0] = 0
        for i in range(1, n1 + 1):
            dp[i][0] = incr(dp[i - 1][0], nums1[i - 1])
        for j in range(1, n2 + 1):
            dp[0][j] = incr(dp[0][j - 1], nums2[j - 1])

        for i, j in product(range(1, n1 + 1), range(1, n2 + 1)):
            dp[i][j] = min(incr(dp[i - 1][j], nums1[i - 1]),
                           incr(dp[i][j - 1], nums2[j - 1]))

        return dp[n1][n2]