from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # Number of rows
        num_rows = len(words)
        
        # Iterate over each row
        for i in range(num_rows):
            # Iterate over each character in the current row
            for j in range(len(words[i])):
                # Check if the corresponding column exists and has the required character
                if j >= num_rows or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True