class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeta(x):
            res = 0
            while x > 0:
                x //= 5
                res += x
            return res
        
        def left_bound(k):
            left, right = 0, 5 * k
            while left < right:
                mid = (left + right) // 2
                if zeta(mid) < k:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        if k == 0:
            return 5
        
        lb = left_bound(k)
        return 0 if zeta(lb) != k else 5