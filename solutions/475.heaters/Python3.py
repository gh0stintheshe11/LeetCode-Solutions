from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radii = []
        
        for house in houses:
            left, right = 0, len(heaters) - 1
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
            dist1 = abs(heaters[left] - house)
            if left > 0:
                dist2 = abs(heaters[left - 1] - house)
                radii.append(min(dist1, dist2))
            else:
                radii.append(dist1)
                
        return max(radii)