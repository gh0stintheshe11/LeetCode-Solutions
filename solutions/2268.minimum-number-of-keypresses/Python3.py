class Solution:
    def minimumKeypresses(self, s: str) -> int:
        from collections import Counter
        # Get the frequency of each character in the string
        freq = Counter(s)
        
        # Sort the characters by frequency in descending order
        freq_sorted = sorted(freq.values(), reverse=True)
        
        total_keypresses = 0
        # Iterate over each frequency using a zero-based index
        for i, f in enumerate(freq_sorted):
            # Calculate how many keypresses are needed for this character
            # Each button has 3 positions, and each position requires 1 more keypress
            keypresses = (i // 9) + 1
            # Add to total keypresses
            total_keypresses += f * keypresses

        return total_keypresses