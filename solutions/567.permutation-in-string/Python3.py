class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len1])
        
        if s1_count == s2_count:
            return True
        
        for i in range(len1, len2):
            s2_count[s2[i]] += 1
            s2_count[s2[i - len1]] -= 1
            if s2_count[s2[i - len1]] == 0:
                del s2_count[s2[i - len1]]
            
            if s1_count == s2_count:
                return True
        
        return False