from typing import List
from collections import defaultdict

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        changes = defaultdict(int)
        
        for position, range_ in lights:
            start = position - range_
            end = position + range_
            changes[start] += 1
            changes[end + 1] -= 1
        
        max_brightness = 0
        current_brightness = 0
        brightest_position = float('inf')
        
        for position in sorted(changes.keys()):
            current_brightness += changes[position]
            if current_brightness > max_brightness:
                max_brightness = current_brightness
                brightest_position = position
        
        return brightest_position