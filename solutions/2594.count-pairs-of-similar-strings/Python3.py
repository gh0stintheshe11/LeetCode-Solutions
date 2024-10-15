class Solution:
    def similarPairs(self, words: List[str]) -> int:
        from collections import defaultdict
        
        # Create a hashmap to store frequency of unique character sets.
        freq = defaultdict(int)
        
        # Count frequency of each unique character set
        for word in words:
            key = frozenset(word)
            freq[key] += 1
        
        # Count similar pairs
        result = 0
        for count in freq.values():
            if count > 1:
                # If n elements have the same character set,
                # then (n choose 2) pairs can be formed.
                result += (count * (count - 1)) // 2
        
        return result