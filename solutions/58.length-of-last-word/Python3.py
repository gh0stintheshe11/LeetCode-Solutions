class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Step 1: Trim the string to remove trailing spaces
        s = s.rstrip()
        
        # Step 2: Split the string into words
        words = s.split(' ')
        
        # Step 3: Find the last word
        last_word = words[-1]
        
        # Step 4: Return the length of the last word
        return len(last_word)
