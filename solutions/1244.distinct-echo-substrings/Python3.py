class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        seen = set()
        
        for length in range(1, n // 2 + 1):
            hash1 = 0
            hash2 = 0
            base = 31
            mod = 10**9 + 7
            base_l = 1
            
            for i in range(length):
                hash1 = (hash1 * base + ord(text[i])) % mod
                hash2 = (hash2 * base + ord(text[length + i])) % mod
                if i < length - 1:
                    base_l = (base_l * base) % mod
            
            for i in range(length, n - length + 1):
                if hash1 == hash2:
                    if text[i - length:i] == text[i:i + length]:
                        seen.add(text[i - length:i + length])
                
                if i < n - length:
                    hash1 = ((hash1 - ord(text[i - length]) * base_l) * base + ord(text[i])) % mod
                    hash2 = ((hash2 - ord(text[i]) * base_l) * base + ord(text[i + length])) % mod
        
        return len(seen)