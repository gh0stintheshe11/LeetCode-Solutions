class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def canCut(mid):
            total = 0
            for ribbon in ribbons:
                total += ribbon // mid
            return total >= k
        
        left, right = 1, max(ribbons)
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canCut(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return best