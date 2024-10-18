class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        max_score, current_sum = 0, 0
        left = 0
        
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            seen.add(nums[right])
            current_sum += nums[right]
            max_score = max(max_score, current_sum)
        
        return max_score