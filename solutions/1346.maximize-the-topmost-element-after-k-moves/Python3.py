from typing import List

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # If k is 0, the top element remains unchanged
        if k == 0:
            return nums[0] if n > 0 else -1
        
        # If we have only one element and k is odd, the pile will be empty
        if n == 1:
            return -1 if k % 2 == 1 else nums[0]
        
        # If k is larger than the size of array, we can only leave out the first element,
        # meaning we can only pick elements from the first k-1 elements.
        if k > n:
            return max(nums)
        
        # For k <= n, the problem is to pick the max element from the first k elements
        # or pick nums[k] if k < n.
        max_in_first_k_minus_one = max(nums[:k - 1]) if k > 1 else -1
        return max(max_in_first_k_minus_one, nums[k] if k < n else -1)