from typing import List

class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        def possible(x: float) -> bool:
            out = sum(max(0, b - x) for b in buckets)
            in_need = sum(max(0, x - b) for b in buckets)
            return out * (1 - loss / 100) >= in_need

        low, high = 0.0, max(buckets)
        precision = 1e-6
        while high - low > precision:
            mid = (low + high) / 2
            if possible(mid):
                low = mid
            else:
                high = mid
        return low