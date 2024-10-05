from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Count the frequency of each character in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Compare the two frequency counters
        return count_s == count_t
