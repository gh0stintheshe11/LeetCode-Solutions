from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        k_distant_indices = set()
        
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                    k_distant_indices.add(j)
        
        return sorted(k_distant_indices)