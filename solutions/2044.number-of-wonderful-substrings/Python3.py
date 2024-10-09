class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = {0: 1}
        mask = 0
        count = 0
        for ch in word:
            # Update the mask for the current character
            mask ^= 1 << (ord(ch) - ord('a'))
            # Count the current mask directly
            count += freq.get(mask, 0)
            # Try to flip each bit
            for i in range(10):
                count += freq.get(mask ^ (1 << i), 0)
            # Update the frequency map
            freq[mask] = freq.get(mask, 0) + 1
        return count