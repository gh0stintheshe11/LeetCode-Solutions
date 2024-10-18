import heapq
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        # Convert target into a max heap (using negatives for a max-heap in Python)
        total_sum = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)

        while True:
            largest = -heapq.heappop(target)
            rest_sum = total_sum - largest

            if largest == 1 or rest_sum == 1:
                return True

            if largest < rest_sum or rest_sum == 0 or largest % rest_sum == 0:
                return False

            largest %= rest_sum
            total_sum = rest_sum + largest
            heapq.heappush(target, -largest)