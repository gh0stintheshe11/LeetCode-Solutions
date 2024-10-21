class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        
        prefix_min = [float('inf')] * n
        suffix_min = [float('inf')] * n
        
        prefix_min[0] = nums[0]
        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], nums[i])
        
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
        
        min_sum = float('inf')
        for j in range(1, n - 1):
            if nums[j] > prefix_min[j - 1] and nums[j] > suffix_min[j + 1]:
                min_sum = min(min_sum, prefix_min[j - 1] + nums[j] + suffix_min[j + 1])
        
        return min_sum if min_sum != float('inf') else -1