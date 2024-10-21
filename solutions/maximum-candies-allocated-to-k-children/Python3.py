class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_distribute(candies, k, mid):
            total = 0
            for candy in candies:
                total += candy // mid
                if total >= k:
                    return True
            return total >= k
        
        left, right = 1, max(candies)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_distribute(candies, k, mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result