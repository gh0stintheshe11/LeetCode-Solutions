class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_less_equal(x):
            return sum(min(x // i, n) for i in range(1, m + 1))
        
        low, high = 1, m * n
        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low