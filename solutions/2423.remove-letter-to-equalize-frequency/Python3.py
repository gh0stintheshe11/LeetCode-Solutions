class Solution:
    def equalFrequency(self, word: str) -> bool:
        from collections import Counter
        
        # Count the frequency of each letter in the word
        count = Counter(word)
        
        # List of frequencies
        freq_list = list(count.values())
        
        # Case 1: All frequencies are the same after removing one letter
        # Check if we can make all frequencies the same by removing one occurrence from any character
        for i in range(len(freq_list)):
            # Copy the frequency list and reduce one from one letter frequency
            freq_copy = freq_list.copy()
            freq_copy[i] -= 1
            
            # Remove the frequencies of 0 because removing the last instance of a letter would result in frequency 0
            freq_copy = [f for f in freq_copy if f > 0]
            
            # If all remaining frequencies are the same, return True
            if len(set(freq_copy)) == 1:
                return True
        
        return False