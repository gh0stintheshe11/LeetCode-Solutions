from typing import List

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        refills = 0
        currentA, currentB = capacityA, capacityB
        left, right = 0, n - 1
        
        while left <= right:
            if left == right:  # They meet at the same plant
                if currentA >= currentB:
                    if currentA < plants[left]:
                        refills += 1
                else:
                    if currentB < plants[right]:
                        refills += 1
                break
            
            if currentA < plants[left]:
                refills += 1
                currentA = capacityA
            currentA -= plants[left]
            
            if currentB < plants[right]:
                refills += 1
                currentB = capacityB
            currentB -= plants[right]
            
            left += 1
            right -= 1
        
        return refills