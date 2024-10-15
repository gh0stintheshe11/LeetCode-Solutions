class Solution:
    def betterCompression(self, compressed: str) -> str:
        from collections import defaultdict
        import re
        
        frequency_map = defaultdict(int)
        
        i = 0
        n = len(compressed)
        while i < n:
            letter = compressed[i]
            i += 1
            j = i
            while j < n and compressed[j].isdigit():
                j += 1
            freq = int(compressed[i:j])
            frequency_map[letter] += freq
            i = j
        
        result = []
        for char in sorted(frequency_map.keys()):
            result.append(f"{char}{frequency_map[char]}")
        
        return ''.join(result)