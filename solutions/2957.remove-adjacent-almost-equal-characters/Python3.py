class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        operations = 0
        
        i = 0
        while i < n - 1:
            if abs(ord(word[i]) - ord(word[i + 1])) <= 1:
                operations += 1
                i += 1  # Skip extra because two consecutive matched
            i += 1
        
        return operations