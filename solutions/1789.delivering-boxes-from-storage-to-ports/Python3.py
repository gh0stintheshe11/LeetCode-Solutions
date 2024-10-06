from heapq import heappop, heappush
from typing import List

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        deliveries = [0] * (n + 1)
        dp = [0] * (n + 1)

        total_weight = 0
        total_boxes = 0
        delivery_cost = 0

        left = 0
        for right in range(n):
            port, weight = boxes[right]

            if right > 0 and port != boxes[right - 1][0]:
                delivery_cost += 1

            total_weight += weight
            total_boxes += 1

            while total_boxes > maxBoxes or total_weight > maxWeight or (left < right and dp[left] == dp[left + 1]):
                total_weight -= boxes[left][1]
                total_boxes -= 1
                if boxes[left][0] != boxes[left + 1][0]:
                    delivery_cost -= 1
                left += 1

            deliveries[right + 1] = delivery_cost

            dp[right + 1] = dp[left] + deliveries[right + 1] + 2

        return dp[n]