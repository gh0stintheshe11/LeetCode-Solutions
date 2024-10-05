class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated_a = a
        count = 1
        
        while len(repeated_a) < len(b):
            repeated_a += a
            count += 1
        
        if b in repeated_a:
            return count
        
        repeated_a += a
        count += 1
        
        if b in repeated_a:
            return count
        
        return -1