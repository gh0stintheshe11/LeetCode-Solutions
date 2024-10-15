from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        # Preprocess nums to find all indices of x
        indices = []
        for i, num in enumerate(nums):
            if num == x:
                indices.append(i)
        
        # Process each query
        result = []
        for q in queries:
            if q <= len(indices):
                result.append(indices[q - 1])
            else:
                result.append(-1)
        
        return result