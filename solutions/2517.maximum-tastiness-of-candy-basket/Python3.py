from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        
        def canAchieve(x):
            count, last = 1, price[0]
            for i in range(1, len(price)):
                if price[i] - last >= x:
                    count += 1
                    last = price[i]
                    if count == k:
                        return True
            return False
        
        left, right = 0, price[-1] - price[0]
        while left < right:
            mid = left + (right - left + 1) // 2
            if canAchieve(mid):
                left = mid
            else:
                right = mid - 1
        
        return left