from typing import List
from collections import defaultdict

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Initialize frequency dictionary and variables for max score and current score
        freq = defaultdict(int)
        current_score = 0
        max_score = 0
        
        # Calculate frequency score for the first window of size k
        for i in range(k):
            num = nums[i]
            freq[num] += 1
            if freq[num] == 1:
                current_score = (current_score + num) % MOD
            else:
                current_score = (current_score - pow(num, freq[num] - 1, MOD) + pow(num, freq[num], MOD)) % MOD
        
        max_score = current_score
        
        # Slide the window across the array
        for i in range(k, n):
            # Add new element to the window
            new_num = nums[i]
            freq[new_num] += 1
            if freq[new_num] == 1:
                current_score = (current_score + new_num) % MOD
            else:
                current_score = (current_score - pow(new_num, freq[new_num] - 1, MOD) + pow(new_num, freq[new_num], MOD)) % MOD
            
            # Remove the element that goes out of the window
            old_num = nums[i - k]
            freq[old_num] -= 1
            if freq[old_num] == 0:
                current_score = (current_score - old_num) % MOD
                del freq[old_num]
            else:
                current_score = (current_score - pow(old_num, freq[old_num] + 1, MOD) + pow(old_num, freq[old_num], MOD)) % MOD
            
            # Update max_score
            max_score = max(max_score, current_score)
        
        return max_score