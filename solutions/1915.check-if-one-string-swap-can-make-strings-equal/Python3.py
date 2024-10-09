class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        # Find indices where s1 and s2 differ
        diff_indices = [i for i in range(len(s1)) if s1[i] != s2[i]]
        
        # Check if there are exactly 2 differences 
        # and swapping these makes the strings equal
        if len(diff_indices) == 2:
            i, j = diff_indices
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        return False