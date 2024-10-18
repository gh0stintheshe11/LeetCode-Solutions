from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_captures = 0
        n = len(forts)
        i = 0
        
        while i < n:
            if forts[i] == 1:  # Start from your fort
                j = i + 1
                capture_count = 0
                
                # Move to the right
                while j < n and forts[j] == 0:
                    capture_count += 1
                    j += 1
                
                # Check if you have found the other fort
                if j < n and forts[j] == -1:
                    max_captures = max(max_captures, capture_count)
            
            elif forts[i] == -1:  # Start from an enemy fort
                j = i + 1
                capture_count = 0
                
                # Move to the right
                while j < n and forts[j] == 0:
                    capture_count += 1
                    j += 1
                
                # Check if you have found your fort
                if j < n and forts[j] == 1:
                    max_captures = max(max_captures, capture_count)
                    
            # Move to the next potential starting point
            i += 1
        
        return max_captures