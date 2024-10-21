class Solution:
    def numSplits(self, s: str) -> int:
        from collections import Counter
        
        left_counts = Counter()
        right_counts = Counter(s)
        
        left_unique = 0
        right_unique = len(right_counts)
        
        good_splits = 0
        
        for char in s:
            # Update left side
            if left_counts[char] == 0:
                left_unique += 1
            left_counts[char] += 1
            
            # Update right side
            right_counts[char] -= 1
            if right_counts[char] == 0:
                right_unique -= 1
            
            # Check if current split is good
            if left_unique == right_unique:
                good_splits += 1
        
        return good_splits