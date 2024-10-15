from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        
        # Initialize the dp arrays
        dpA = [0] * n
        dpB = [0] * n
        
        # Set the base cases
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]
        
        # Fill the dp arrays
        for i in range(1, n):
            dpA[i] = energyDrinkA[i] + max(dpA[i-1], dpB[i-2] if i > 1 else 0)
            dpB[i] = energyDrinkB[i] + max(dpB[i-1], dpA[i-2] if i > 1 else 0)
        
        # The result is the maximum boost we can achieve in the last hour (either drinking A or B)
        return max(dpA[-1], dpB[-1])