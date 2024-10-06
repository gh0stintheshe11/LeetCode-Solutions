from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        
        # Step 1: Calculate the first and last occurrence of each character
        first = {}
        last = {}
        
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
        
        # Step 2: Finding valid intervals
        valid_intervals = []
        
        for char in first:
            start = first[char]
            end = last[char]
            j = start
            
            # Extend the interval to include all occurrences of characters in it
            while j <= end:
                if first[s[j]] < start:
                    start = first[s[j]]
                if last[s[j]] > end:
                    end = last[s[j]]
                j += 1
            
            if start == first[char]:  # Confirm that we have the minimal valid interval for this character
                valid_intervals.append((start, end))
        
        # Step 3: Sort intervals by the end position
        valid_intervals.sort(key=lambda x: x[1])
        
        # Step 4: Select non-overlapping intervals
        result = []
        prev_end = -1
        
        for start, end in valid_intervals:
            if start > prev_end:  # If this interval doesn't overlap with the previously chosen one
                result.append(s[start:end + 1])
                prev_end = end
        
        return result