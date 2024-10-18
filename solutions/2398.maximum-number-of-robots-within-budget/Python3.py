from collections import deque
from typing import List

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        max_charge = deque()
        total_running_cost = 0
        left = 0
        max_robots = 0

        for right in range(n):
            total_running_cost += runningCosts[right]
            
            while max_charge and chargeTimes[max_charge[-1]] <= chargeTimes[right]:
                max_charge.pop()
            max_charge.append(right)
            
            while max_charge and (chargeTimes[max_charge[0]] + (right - left + 1) * total_running_cost > budget):
                if max_charge[0] == left:
                    max_charge.popleft()
                total_running_cost -= runningCosts[left]
                left += 1

            max_robots = max(max_robots, right - left + 1)

        return max_robots