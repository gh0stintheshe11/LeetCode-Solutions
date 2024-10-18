from collections import defaultdict
from sortedcontainers import SortedList
from typing import List

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        count_map = defaultdict(int)
        freq_tracker = SortedList()
        result = []
        
        for i in range(len(nums)):
            id_num, freq_change = nums[i], freq[i]
            
            # If the ID already has a count, update the frequency tracker
            if count_map[id_num] > 0:
                freq_tracker.remove(count_map[id_num])
            
            # Update the count for the current ID
            count_map[id_num] += freq_change
            
            # Add the updated count back to the frequency tracker if it's positive
            if count_map[id_num] > 0:
                freq_tracker.add(count_map[id_num])
            
            # Determine the maximum frequency at the current step
            if freq_tracker:
                result.append(freq_tracker[-1])
            else:
                result.append(0)
        
        return result