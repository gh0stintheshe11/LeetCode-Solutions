from math import sqrt

class Solution:
    def minOperations(self, k: int) -> int:
        res = int(2 * sqrt(k) - 2)
        return res if self.issquare(k) else res + 1

    def issquare(self, k):
        if k == 1: return True
        left = 1
        right = k // 2
        while left <= right:
            mid = left + (right-left)//2
            if mid * mid > k:
                right = mid - 1
            elif mid * mid < k:
                left = mid + 1
            else:
                return True
        return False