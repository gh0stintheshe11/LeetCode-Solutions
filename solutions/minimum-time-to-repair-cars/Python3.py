from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepairInTime(time: int) -> bool:
            total_cars_repaired = 0
            for rank in ranks:
                total_cars_repaired += int((time // rank) ** 0.5)
                if total_cars_repaired >= cars:
                    return True
            return total_cars_repaired >= cars

        low, high = 0, max(ranks) * cars * cars
        while low < high:
            mid = (low + high) // 2
            if canRepairInTime(mid):
                high = mid
            else:
                low = mid + 1

        return low