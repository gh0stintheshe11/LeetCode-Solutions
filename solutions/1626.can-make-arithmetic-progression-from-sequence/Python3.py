from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Calculate the common difference
        common_difference = arr[1] - arr[0]
        
        # Step 3: Check if all consecutive elements have the same difference
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != common_difference:
                return False
        
        return True