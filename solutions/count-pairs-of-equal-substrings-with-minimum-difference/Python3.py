class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        from collections import defaultdict
        
        first_occurrence = {}
        last_occurrence = {}
        
        for i, char in enumerate(firstString):
            if char not in first_occurrence:
                first_occurrence[char] = i
        
        for i, char in enumerate(secondString):
            last_occurrence[char] = i
        
        min_diff = float('inf')
        count = 0
        
        for char in first_occurrence:
            if char in last_occurrence:
                i = first_occurrence[char]
                b = last_occurrence[char]
                current_diff = i - b
                if current_diff < min_diff:
                    min_diff = current_diff
                    count = 1
                elif current_diff == min_diff:
                    count += 1
        
        return count