class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # Create a dictionary that maps each character to its index on the keyboard
        char_index = {char: idx for idx, char in enumerate(keyboard)}
        
        # Start at the initial position of the finger, which is at index 0
        current_pos = 0
        time = 0
        
        # Iterate through each character in the word
        for char in word:
            # Move the finger to the position of the current character
            next_pos = char_index[char]
            # Calculate the time taken to move to the next position
            time += abs(next_pos - current_pos)
            # Update the current position to the new position
            current_pos = next_pos
        
        return time