from typing import List

class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        brightness = [0] * (n + 1)  # Extra space to handle last range properly
        
        for position, range_ in lights:
            start = max(0, position - range_)
            end = min(n - 1, position + range_)
            
            brightness[start] += 1
            if end + 1 < n:
                brightness[end + 1] -= 1
                
        current_brightness = 0
        count = 0
        
        for i in range(n):
            current_brightness += brightness[i]
            if current_brightness >= requirement[i]:
                count += 1
                
        return count