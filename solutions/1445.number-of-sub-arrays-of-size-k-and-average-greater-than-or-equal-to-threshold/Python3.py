from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = threshold * k
        current_sum = sum(arr[:k])
        count = 0
        
        if current_sum >= target_sum:
            count += 1
        
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]
            if current_sum >= target_sum:
                count += 1
        
        return count