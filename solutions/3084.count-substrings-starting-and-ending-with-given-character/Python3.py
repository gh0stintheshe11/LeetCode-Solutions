class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count_c = 0
        total_substrings = 0
        
        # Iterate through the string to count occurrences of character c
        for char in s:
            if char == c:
                # For every occurrence of 'c', increment count_c and add it to total substrings
                count_c += 1
                total_substrings += count_c
                
        return total_substrings