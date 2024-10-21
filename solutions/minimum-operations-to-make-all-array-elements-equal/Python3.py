from typing import List

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [0] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        result = []
        
        for q in queries:
            idx = self.binary_search(nums, q)
            left_sum = q * idx - prefix_sum[idx] 
            right_sum = (prefix_sum[len(nums)] - prefix_sum[idx]) - q * (len(nums) - idx)
            result.append(left_sum + right_sum)
        
        return result
    
    def binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left