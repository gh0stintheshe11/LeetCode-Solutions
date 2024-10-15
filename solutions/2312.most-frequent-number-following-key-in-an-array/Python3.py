class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        from collections import defaultdict
        
        count = defaultdict(int)
        
        for i in range(len(nums) - 1):
            if nums[i] == key:
                count[nums[i + 1]] += 1
        
        max_target = max(count.keys(), key=lambda x: count[x])
        return max_target