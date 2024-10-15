from typing import List

class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def count_subarrays_less_equal(target):
            count, curr_sum, start = 0, 0, 0
            for end in range(len(nums)):
                curr_sum += nums[end]
                while curr_sum > target:
                    curr_sum -= nums[start]
                    start += 1
                count += end - start + 1
            return count
        
        left, right = min(nums), sum(nums)
        result = right
        
        while left <= right:
            mid = left + (right - left) // 2
            if count_subarrays_less_equal(mid) >= k:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result