class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        current_hash = 0
        power_k = 1
        
        # Calculate power^k % modulo
        for _ in range(k):
            power_k = power_k * power % modulo
        
        # Calculate the hash for the last k-length substring
        for i in range(n - 1, n - k - 1, -1):
            current_hash = (current_hash * power + (ord(s[i]) - ord('a') + 1)) % modulo
        
        # Tracks the result's starting index as we loop backwards
        result_index = n - k
        
        if current_hash == hashValue:
            result_index = n - k
        
        # Iterate the string backwards with a rolling hash
        for start in range(n - k - 1, -1, -1):
            # Remove the effect of the character s[start + k]
            current_hash = (current_hash * power + (ord(s[start]) - ord('a') + 1) -
                            (ord(s[start + k]) - ord('a') + 1) * power_k % modulo + modulo) % modulo
            
            if current_hash == hashValue:
                result_index = start
        
        return s[result_index:result_index + k]