from typing import List

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def canPlaceGasStations(max_dist):
            count = 0
            for i in range(len(stations) - 1):
                count += int((stations[i + 1] - stations[i]) / max_dist)
            return count <= k
        
        left, right = 0, 10**8
        while right - left > 1e-6:
            mid = (left + right) / 2
            if canPlaceGasStations(mid):
                right = mid
            else:
                left = mid
        
        return right