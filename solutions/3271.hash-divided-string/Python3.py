class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        result = []
        
        for i in range(0, n, k):
            substring = s[i:i+k]
            sum_hash = sum(ord(char) - ord('a') for char in substring)
            hashed_char = chr((sum_hash % 26) + ord('a'))
            result.append(hashed_char)
        
        return ''.join(result)