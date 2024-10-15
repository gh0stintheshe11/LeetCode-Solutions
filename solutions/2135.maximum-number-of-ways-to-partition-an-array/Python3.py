from typing import List

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        prefix_sum = 0
        left_count = {}
        right_count = {}
        
        for i in range(n-1):
            prefix_sum += nums[i]
            right_count[prefix_sum] = right_count.get(prefix_sum, 0) + 1
        
        max_ways = right_count.get(total_sum // 2, 0) if total_sum % 2 == 0 else 0
        
        prefix_sum = 0
        for i in range(n):
            if i > 0:
                prefix_sum += nums[i - 1]
                right_count[prefix_sum] -= 1
                if right_count[prefix_sum] == 0:
                    del right_count[prefix_sum]
                left_count[prefix_sum] = left_count.get(prefix_sum, 0) + 1

            change = k - nums[i]
            new_sum = total_sum + change
            if new_sum % 2 == 0:
                target = new_sum // 2
                ways = left_count.get(target, 0) + right_count.get(target - change, 0)
                max_ways = max(max_ways, ways)

        return max_ways