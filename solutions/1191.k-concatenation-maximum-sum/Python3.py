class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Helper function to find the maximum subarray sum using Kadane's algorithm
        def maxSubArraySum(nums):
            max_so_far = max_ending_here = 0
            for x in nums:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        # Maximum subarray sum for a single array
        single_kadane = maxSubArraySum(arr)
        
        if k == 1:
            return single_kadane % MOD
        
        # Calculate prefix, suffix, and total array sums
        array_sum = sum(arr)
        
        prefix_sum = 0
        max_prefix_sum = arr[0]
        for num in arr:
            prefix_sum += num
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
        
        suffix_sum = 0
        max_suffix_sum = arr[-1]
        for num in reversed(arr):
            suffix_sum += num
            max_suffix_sum = max(max_suffix_sum, suffix_sum)
        
        # Calculate maximum sum for k > 1
        if array_sum > 0:
            result = max(single_kadane, max_prefix_sum + max_suffix_sum + (k - 2) * array_sum)
        else:
            result = max(single_kadane, max_prefix_sum + max_suffix_sum)
        
        return result % MOD