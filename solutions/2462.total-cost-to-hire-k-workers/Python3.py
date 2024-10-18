from heapq import heappush, heappop
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        total_cost = 0
        left_heap = []
        right_heap = []
        left_area_end = candidates - 1
        right_area_start = n - candidates

        for i in range(candidates):
            heappush(left_heap, (costs[i], i))
        for i in range(max(candidates, right_area_start), n):
            heappush(right_heap, (costs[i], i))

        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0][0] <= right_heap[0][0]):
                cost, index = heappop(left_heap)
                total_cost += cost
                if left_area_end + 1 < right_area_start:
                    left_area_end += 1
                    heappush(left_heap, (costs[left_area_end], left_area_end))
            else:
                cost, index = heappop(right_heap)
                total_cost += cost
                if right_area_start > left_area_end + 1:
                    right_area_start -= 1
                    heappush(right_heap, (costs[right_area_start], right_area_start))

        return total_cost