from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store the cumulative sum frequencies
        sum_freq = {0: 1}
        cumulative_sum = 0
        count = 0
        
        for num in nums:
            # Update the cumulative sum
            cumulative_sum += num
            
            # Check if there is a subarray (ending at the current index) which sums to k
            if (cumulative_sum - k) in sum_freq:
                count += sum_freq[cumulative_sum - k]
            
            # Update the frequency of the current cumulative sum in the dictionary
            if cumulative_sum in sum_freq:
                sum_freq[cumulative_sum] += 1
            else:
                sum_freq[cumulative_sum] = 1
        
        return count
