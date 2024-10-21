class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        from functools import lru_cache
        n = len(nums)
        
        @lru_cache(None)
        def dfs(i, slots):
            if i == n:
                return 0
            
            max_and_sum = 0
            for slot in range(numSlots):
                for option in range(2):
                    if (slots >> (2 * slot + option)) & 1 == 0:  # Check if slot is available
                        new_slots = slots | (1 << (2 * slot + option))
                        max_and_sum = max(max_and_sum, (nums[i] & (slot + 1)) + dfs(i + 1, new_slots))
            return max_and_sum
        
        return dfs(0, 0)