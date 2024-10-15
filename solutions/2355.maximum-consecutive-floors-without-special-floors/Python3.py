from typing import List

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        # Sort the list of special floors
        special.sort()
        
        # Initialize the maximum consecutive floors to zero
        max_consecutive = 0
        
        # Check the range before the first special floor
        max_consecutive = max(max_consecutive, special[0] - bottom)
        
        # Check between consecutive special floors
        for i in range(1, len(special)):
            max_consecutive = max(max_consecutive, special[i] - special[i - 1] - 1)
        
        # Check the range after the last special floor
        max_consecutive = max(max_consecutive, top - special[-1])
        
        return max_consecutive