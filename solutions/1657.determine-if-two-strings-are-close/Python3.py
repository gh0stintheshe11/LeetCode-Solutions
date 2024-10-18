class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        
        # If the lengths are different, they can't be close
        if len(word1) != len(word2):
            return False
        
        # Frequency count of characters in word1 and word2
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # Both words must have the same set of unique characters
        if set(count1.keys()) != set(count2.keys()):
            return False
        
        # Both words must have the same frequency distribution of characters
        if sorted(count1.values()) != sorted(count2.values()):
            return False
        
        return True