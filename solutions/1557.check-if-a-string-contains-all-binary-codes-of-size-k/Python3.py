class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        needed = 1 << k
        seen = set()
        
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            if substring not in seen:
                seen.add(substring)
                needed -= 1
                if needed == 0:
                    return True
        
        return False