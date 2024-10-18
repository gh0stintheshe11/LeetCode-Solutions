class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter

        # Count the frequency of each character in the word
        freq = Counter(word)
        
        # Extract the frequencies and sort them in descending order
        sorted_freq = sorted(freq.values(), reverse=True)

        total_pushes = 0
        # We have 8 keys, so we can type 8 characters with 1 push each, and so on
        for i, f in enumerate(sorted_freq):
            key_pushes = (i // 8) + 1
            total_pushes += key_pushes * f

        return total_pushes