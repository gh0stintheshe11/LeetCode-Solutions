class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 1
        
        for char in s:
            if char in seen:
                count += 1
                seen.clear()
            seen.add(char)
        
        return count