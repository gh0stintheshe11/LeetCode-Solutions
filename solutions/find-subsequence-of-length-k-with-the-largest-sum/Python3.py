from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Get indices of the k largest elements based on their values
        largest_indices = sorted(range(len(nums)), key=lambda i: nums[i], reverse=True)[:k]
        
        # Sort indices to maintain the order of the subsequence as it appears in the original list
        largest_indices.sort()
        
        # Return the subsequence
        return [nums[i] for i in largest_indices]