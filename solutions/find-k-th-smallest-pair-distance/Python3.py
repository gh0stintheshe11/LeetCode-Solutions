from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_pairs(max_distance):
            count, j = 0, 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= max_distance:
                    j += 1
                count += j - i - 1
            return count
        
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= k:
                high = mid
            else:
                low = mid + 1
                
        return low