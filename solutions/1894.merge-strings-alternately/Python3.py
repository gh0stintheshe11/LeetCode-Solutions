class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize pointers for both strings
        i, j = 0, 0
        # Initialize the result list to store the merged characters
        result = []
        
        # Loop until we reach the end of both strings
        while i < len(word1) and j < len(word2):
            # Append characters alternately from word1 and word2
            result.append(word1[i])
            result.append(word2[j])
            # Move the pointers forward
            i += 1
            j += 1
        
        # If there are remaining characters in word1, append them
        if i < len(word1):
            result.append(word1[i:])
        
        # If there are remaining characters in word2, append them
        if j < len(word2):
            result.append(word2[j:])
        
        # Join the list into a single string and return
        return ''.join(result)