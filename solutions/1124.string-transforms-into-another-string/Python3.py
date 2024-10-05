class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        
        if len(set(str2)) == 26:
            return False
        
        mapping = {}
        for c1, c2 in zip(str1, str2):
            if c1 in mapping and mapping[c1] != c2:
                return False
            mapping[c1] = c2
        
        return True