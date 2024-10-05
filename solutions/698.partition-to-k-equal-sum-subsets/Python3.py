from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        nums.sort(reverse=True)
        buckets = [0] * k
        
        def backtrack(index):
            if index == len(nums):
                return all(bucket == target for bucket in buckets)
            
            for i in range(k):
                if buckets[i] + nums[index] <= target:
                    buckets[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    buckets[i] -= nums[index]
                
                if buckets[i] == 0:
                    break
            
            return False
        
        return backtrack(0)