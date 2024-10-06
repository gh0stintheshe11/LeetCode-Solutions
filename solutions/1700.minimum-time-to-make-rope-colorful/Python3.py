from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        i = 0
        n = len(colors)
        
        while i < n:
            j = i
            max_time = 0
            sum_time = 0
            
            while j < n and colors[j] == colors[i]:
                max_time = max(max_time, neededTime[j])
                sum_time += neededTime[j]
                j += 1
                
            total_time += (sum_time - max_time)
            i = j
            
        return total_time