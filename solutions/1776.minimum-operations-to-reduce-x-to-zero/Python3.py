class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        current_sum = 0
        max_length = -1
        left = 0
        
        for right, num in enumerate(nums):
            current_sum += num
            
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            
            if current_sum == target:
                max_length = max(max_length, right - left + 1)
        
        return len(nums) - max_length if max_length != -1 else -1